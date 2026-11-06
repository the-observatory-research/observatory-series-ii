#!/usr/bin/env python3
"""Build a factual *present/missing* inventory for Series II source files.
Optional exact-format comparison uses a library standalone implementation and does
NOT independently establish that the implementation was the one used in 2026.
"""
import argparse, hashlib, csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arm_b_normalizer import normalize
MODELS=['ChatGPT','DeepSeek','Gemini','Claude','Grok','Meta AI']

def main():
  ap=argparse.ArgumentParser()
  ap.add_argument('--root',type=Path,default=Path('data'))
  ap.add_argument('--manifest',type=Path,default=Path('evidence-manifest.csv'))
  args=ap.parse_args()
  rows=[]
  for arm in ('A','B'):
    for c in range(1,6):
      for m,model in enumerate(MODELS,1):
        record=f'SII-{arm}-C{c:02d}-M{m:02d}'
        versions=['raw'] if arm=='A' else ['raw','normalized']
        for version in versions:
          folder=args.root/('arm-a' if arm=='A' else 'arm-b')/version
          path=folder/f'{record}-{version}.txt'
          present=path.is_file()
          body=path.read_bytes() if present else b''
          rows.append({'record_id':record,'model':model,'version':version,'file':str(path),
                'status':'present' if present else 'missing','bytes':len(body) if present else '',
                'sha256':hashlib.sha256(body).hexdigest() if present else '',
                'normalizer_comparison':'not_checked'})
  lookup={(r['record_id'],r['version']):r for r in rows}
  for c in range(1,6):
    for m in range(1,7):
      rec=f'SII-B-C{c:02d}-M{m:02d}'
      a,b=lookup[(rec,'raw')],lookup[(rec,'normalized')]
      if a['status']=='present' and b['status']=='present':
        try:
          generated=normalize(Path(a['file']).read_bytes().decode('utf-8')).encode('utf-8')
          b['normalizer_comparison']='match' if generated==Path(b['file']).read_bytes() else 'mismatch'
        except UnicodeDecodeError:
          b['normalizer_comparison']='undecodable_utf8'
  args.manifest.parent.mkdir(parents=True,exist_ok=True)
  with args.manifest.open('w',newline='',encoding='utf-8') as out:
    writer=csv.DictWriter(out,fieldnames=list(rows[0])); writer.writeheader();writer.writerows(rows)
  missing=sum(x['status']=='missing' for x in rows)
  mismatches=sum(x['normalizer_comparison']=='mismatch' for x in rows)
  print(f'Inventory: {len(rows)-missing}/{len(rows)} files present; {missing} missing; {mismatches} normalizer mismatches')
  print(f'Wrote {args.manifest}')
  # Not a replacement for historical frozen-hash verification.
  if mismatches: sys.exit(2)

if __name__=='__main__': main()
