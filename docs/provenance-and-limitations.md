# Provenance, boundaries and release checklist

## Source identification

The files in `docs/original-records/` are carried forward byte-for-byte from files recovered from The Observatory research records in this working session. These are documentation sources, not substitutes for all underlying model response payloads.

- `series-ii-pre-execution-protocol-clarified.md`: archival clarified series-wide protocol (post-execution clarifications appear in the source text).
- `arm-a-execution-log.md`: Arm A execution/audit source, previously recorded as 30/30 complete.
- `arm-b-pre-execution-protocol.md`: early frozen Arm B protocol, including original documented Python approach.
- `arm-b-pre-execution-protocol-clarified.docx`: preserved clarified protocol document.
- `arm-b-execution-log.docx`: preserved execution/audit document. It reports 30/30 transformations, but its visible terminal command coverage alone documents 29 distinct normalizer invocation IDs; absence from that visible log must not be equated with absence of an original file.
- `arm_b_normalizer.py`: an independently located Python file from the research file library; its source implementation uses regex-based blank-line collapsing. The source protocol also records an equivalent-looking loop-based variant. Equivalence should be tested on original fixtures; **do not assume unverified historical version identity**.

## Explicitly missing

- **Arm A raw response payloads:** no individually authenticated `.txt` collection imported into this package.
- **Arm B raw and normalized payloads:** no complete, individually authenticated 30+30 source `.txt` collection imported here.
- **IRP primary artifacts:** the archive catalog references source-integrity, response, freeze-manifest, scoring and adjudication files, but those exact files have not been imported here.
- **Transcript assembly templates:** discovered templates contain bracketed placeholders and are intentionally excluded from `data/` to avoid misrepresenting them as source evidence.

A research conversation PDF about IRP was located but is not treated here as an authoritative substitute for the independent recovery files.

## Before making GitHub public

- [ ] Locate original Arm A raw files, Arm B raw + normalized files, and IRP source files.
- [ ] Confirm model-name, date, filename and session metadata against original sources.
- [ ] Confirm each artifact hash against the applicable historical freeze manifest where available.
- [ ] Compare the Python normalizer to archived historical implementation and expected results.
- [ ] Remove or redact personal identifiers, private logs, credentials, or restricted output.
- [ ] Decide an appropriate copyright/license policy; do not infer permission to redistribute third-party responses.
- [ ] Mark original source files as immutable and any newly derived annotations separately.
- [ ] Replace this starter status with a precise release/version status after review.
