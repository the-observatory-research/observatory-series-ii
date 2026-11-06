# Source evidence import area — currently incomplete

Suggested destinations for verified original records:

```text
data/
  arm-a/raw/SII-A-C01-M01-raw.txt ... SII-A-C05-M06-raw.txt
  arm-b/raw/SII-B-C01-M01-raw.txt ... SII-B-C05-M06-raw.txt
  arm-b/normalized/SII-B-C01-M01-normalized.txt ... SII-B-C05-M06-normalized.txt
  recovery/  # separately structured IRP source, response and scoring material
  expected-records.csv  # generated index, not experimental evidence
```

Do **not** populate these from transcript templates, structural summaries or imagined output. Keep original bytes immutable. Use a copy for verification. The `scripts/verify_evidence.py` utility reports files present/missing and can verify formatting agreement; it does not establish original provenance on its own.
