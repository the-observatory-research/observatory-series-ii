# Experimental design · reader's guide

## Fixed cross-model relay

Series II compared two transmission conditions using the same six-model order over five consecutive cycles. Each of the thirty model positions per arm used a new chat session and the fixed instruction, with the output from each position becoming the next position's input. At a cycle boundary, Meta AI's output advanced to ChatGPT in the next cycle. Neither arm was restarted from the original system during its five cycles.

### Arm A: raw return

The full response was forwarded without formatting normalization. The Arm A execution record distinguishes **preliminary structural sufficiency** from later independently assessed recoverability. Its early 'Independent Recovery: Pending' notation reflects the historical status at that freeze, not the completed status of subsequent work.

### Arm B: deterministic normalization

The response was saved raw, then transformed by a formatting-only normalization operator. The normalized output was forwarded. The operator addresses line endings, Unicode NFC, trailing horizontal whitespace, excess blank lines and leading/trailing blank lines. It does not intentionally parse or repair semantic content. The terminal Arm B output was normalized for archival completeness but not passed forward to another model.

### Independent Recovery Phase (IRP)

A separately configured evaluator was tasked with answering frozen relational questions from the archived descriptions. This evaluates what an independent recipient could recover, which is distinct from whether a source description explicitly contains specified structural details. The scoring and adjudication records must be imported without changing their frozen historical results.

## Critical distinctions

- A fully retained set of nodes/edges/constraints within a source text does **not** automatically prove independent question-answer recovery.
- A valid file list does **not** establish byte-for-byte fidelity to the original model output.
- A normalizer test pass does **not** independently validate the entire cross-model experiment.
- A later audit or analysis does **not** retroactively change the protocol originally used.

Read the exact documents in [`original-records`](original-records/) for historical wording.
