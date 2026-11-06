# The Observatory · Series II — Recursive Relational Stability

**Repository status: source-grounded starter; not yet a complete public experimental dataset.**

Series II is an experiment in recoverability of relational information during repeated, sequential transformations across differentiated language-model systems. This repository provides authentic protocol and execution documentation, a recovered standalone implementation of the Arm B formatting normalizer, and newly authored repository-level checks for its documented behavior.

The original completed research is **not being revised** by this repository. This is an access and reproducibility layer, not a rewritten research report.

## Experimental design

- **Arm A — Raw Relay:** 5 cycles × 6 model positions = 30 transformations; full raw outputs forwarded to the next model.
- **Arm B — Deterministic Formatting Normalization:** 5 × 6 = 30 transformations; raw outputs saved before formatting-only normalization; normalized output forwarded.
- **Model sequence in each cycle:** ChatGPT → DeepSeek → Gemini → Claude → Grok → Meta AI.
- **Independent Recovery Phase:** subsequent isolated evaluations of recoverability from the archived descriptions, with a frozen question/answer instrument and separately adjudicated scores.

Both arms began independently from a specified canonical relational description, used the same frozen transformation instruction, and did not authorize intermediate semantic repair. The model relay itself is a human-facilitated historical experiment; running the included Python program **does not replay the model experiment**.

## Contents

| Path | Contents | Evidence status |
|---|---|---|
| [`docs/original-records/`](docs/original-records/) | Pre-execution specifications, Arm A execution log, Arm B execution log | Files copied from retrieved research sources; original formats/text preserved |
| [`arm_b_normalizer.py`](arm_b_normalizer.py) | Standalone Python normalizer from research file library | Original script bytes preserved; relationship to exact historical deployed revision requires version confirmation |
| [`tests/`](tests/) | Eight newly prepared regression checks | Newly authored; **not** claimed to be original historical test script |
| [`scripts/verify_evidence.py`](scripts/verify_evidence.py) | File inventory and normalized output comparison | Newly authored audit utility |
| [`data/expected-records.csv`](data/expected-records.csv) | Expected transformation identifiers, arms, cycles and model positions | Generated from documented experiment design; not a results file |
| [`data/`](data/) | Landing place for verified raw/normalized records | Source files **not imported yet** |
| [`docs/methodology.md`](docs/methodology.md) | Reading guide | New explanatory documentation, not an experimental source |
| [`docs/provenance-and-limitations.md`](docs/provenance-and-limitations.md) | Publication boundary and missing-data log | Explicitly distinguishes evidence and absence |

## Run the normalizer and tests

Requires Python 3, using only standard-library modules.

```bash
python3 -m unittest discover -s tests -v
python3 arm_b_normalizer.py path/to/SII-B-C01-M01-raw.txt path/to/SII-B-C01-M01-normalized.txt
```

The second command is an **illustration**; the referenced `.txt` record is not bundled here. **Do not overwrite or substitute a historical normalized artifact with a newly computed one**. Test with copies and compare results.

When original `.txt` files have been independently imported:

```bash
python3 scripts/verify_evidence.py --root data --manifest evidence-manifest.csv
```

## What still needs import before publication as a complete evidence package

1. The 30 actual Arm A response `.txt` files. Existing compiled Arm A transcript copies contain `[Paste full raw response verbatim here]` placeholders and are **not** the original raw outputs.
2. The 30 Arm B raw `.txt` outputs and 30 normalized `.txt` outputs. Existing compiled Arm B transcript is an assembly template containing `[SOURCE FILE NOT YET IMPORTED]` markers.
3. Canonical source artifacts for the independent-recovery phase: input manifest, evaluator responses, frozen score matrix, adjudication records, freeze manifest and hashes. Their index is known; not all independently verifiable files were available for this package.
4. Publication/privacy/licensing review of raw responses and metadata.

See [Provenance and limitations](docs/provenance-and-limitations.md) for precise boundaries.

## Study and archive

The Observatory Research Archive: https://publish.obsidian.md/the-observatory/The+Observatory

The completed *What Remains* study is the frozen research source. Any updates to this repository should be labeled as documentation, additional audit tooling, or newly derived analyses—not silent revisions of historical source evidence.

## License and citation

**License not assigned in this starter.** Do not add an open-source license or imply permission to redistribute third-party platform responses until rights are reviewed. Add an accurate citation record / DOI for the corresponding research work once verified.
