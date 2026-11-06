#!/usr/bin/env python3
"""Series II Arm B deterministic formatting-only normalization (N)."""
import argparse
import pathlib
import re
import unicodedata


def normalize(text: str) -> str:
    """Apply the five frozen formatting rules in order."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = unicodedata.normalize('NFC', text)
    text = '\n'.join(line.rstrip(' \t') for line in text.split('\n'))
    text = re.sub(r'\n{4,}', '\n' * 3, text)
    return text.strip('\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=pathlib.Path, help='Raw model output file (UTF-8)')
    parser.add_argument('output', type=pathlib.Path, help='Normalized forwarding payload (UTF-8)')
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Input and output must be different files to preserve raw evidence')
    raw = args.input.read_bytes().decode('utf-8')
    result = normalize(raw)
    args.output.write_bytes(result.encode('utf-8'))
    print(f'Normalized {args.input} -> {args.output}')


if __name__ == '__main__':
    main()
