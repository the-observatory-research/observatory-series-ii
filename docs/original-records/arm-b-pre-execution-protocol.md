# Series II — Arm B (Structured Normalization) Pre-Execution Protocol Specification v1.0

**Title:** Recursive Relational Stability under Deterministic Structural Normalization
**Status:** Pre-Execution Protocol Freeze & Execution Readiness Verified

##  Executive Summary & Parameter Overview

| **Parameter**              | **Specification**                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Experimental Arm**       | **Arm B — Structured Normalization**                                                                              |
| **Model Traversal Order**  | ChatGPT $\rightarrow$ DeepSeek $\rightarrow$ Gemini $\rightarrow$ Claude $\rightarrow$ Grok $\rightarrow$ Meta AI |
| **Cycles per Arm**         | 5 complete cycles (30 total transformations)                                                                      |
| **Session Architecture**   | **30 independent, fresh sessions** (1 per transformation)                                                         |
| **Initial Condition**      | Canonical starting payload $G_0$ (**Un-normalized** prior to $T_{1,1}$)                                           |
| **Normalization Operator** | Validated deterministic Python implementation (`arm_b_normalizer.py`)                                             |
| **Verification Status**    | **8 / 8 Unit Tests PASSED**; CLI File I/O Verified on macOS                                                       |

## 1. The Critical Difference: Arm A vs. Arm B

The fundamental distinction between Arm A and Arm B lies in the inter-node transmission payload handling:

  

$$\begin{aligned} \textbf{Arm A (Raw Return):} \quad & X_{k,j} \xrightarrow{\quad \text{verbatim} \quad} \text{Model}_{j+1} \\ \textbf{Arm B (Structured Normalization):} \quad & X_{k,j}^{\text{raw}} \xrightarrow{\quad \mathcal{N} \quad} X_{k,j}^{\text{normalized}} \xrightarrow{\quad \text{forward} \quad} \text{Model}_{j+1} \end{aligned}$$

- **Non-Intervention Principle:** Operator $\mathcal{N}$ performs **zero** semantic parsing, graph extraction, rule repair, or content reordering. It standardizes whitespace, unicode, and line-ending formatting only.
    
      
    

## 2. Frozen Normalization Operator Rules & Implementation

The normalization operator $\mathcal{N}$ enforces a frozen 5-rule sequential transformation pipeline:

  

1. **Line Endings & Unicode:** Convert all line endings to LF (`\n`) and normalize Unicode characters to NFC standard.
    
      
    
2. **Trailing Whitespace:** Strip trailing spaces and tabs from the end of each line.
    
      
    
3. **Blank Line Collapsing:** Collapse three or more consecutive blank lines down to exactly two blank lines.
    
      
    
4. **Padding Trimming:** Strip leading and trailing blank lines from the start and end of the complete response block.
    
      
    
5. **Structural & Content Preservation:** Preserve all internal line breaks, indentation, words, symbols, negations, and relational constraints verbatim.
    
      
    

### Validated Python Codebase (`arm_b_normalizer.py`)

Python

```
import sys
import unicodedata
from pathlib import Path

def normalize_text(text: str) -> str:
    # Rule 1: LF line endings & Unicode NFC
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = unicodedata.normalize('NFC', text)
    
    # Rule 2: Strip trailing spaces/tabs per line
    lines = [line.rstrip(' \t') for line in text.split('\n')]
    text = '\n'.join(lines)
    
    # Rule 3: Collapse 3+ consecutive blank lines to exactly 2
    while '\n\n\n\n' in text:
        text = text.replace('\n\n\n\n', '\n\n\n')
        
    # Rule 4: Strip leading and trailing blank lines
    text = text.strip('\n')
    return text

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 arm_b_normalizer.py <raw_input_file> <normalized_output_file>")
        sys.exit(1)
        
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    raw_content = input_path.read_bytes().decode('utf-8')
    normalized_content = normalize_text(raw_content)
    output_path.write_bytes(normalized_content.encode('utf-8'))
    print(f"Normalized {input_path} -> {output_path}")

if __name__ == "__main__":
    main()
```

## 3. Local Verification & Environment Audit

Preflight testing was executed on local hardware (`Taras-MacBook-Pro`) under Python 3.14.4.

  

### Test Suite Execution Log (`test_arm_b_normalizer.py`)

Plaintext

```
ecliptx@Taras-MacBook-Pro test-arm-b % python3 -m unittest -v test_arm_b_normalizer.py
test_blank_lines (test_arm_b_normalizer.NormalizationTests.test_blank_lines) ... ok
test_idempotence (test_arm_b_normalizer.NormalizationTests.test_idempotence) ... ok
test_line_endings (test_arm_b_normalizer.NormalizationTests.test_line_endings) ... ok
test_nfc (test_arm_b_normalizer.NormalizationTests.test_nfc) ... ok
test_preserve_indentation (test_arm_b_normalizer.NormalizationTests.test_preserve_indentation) ... ok
test_relational_tokens_unchanged (test_arm_b_normalizer.NormalizationTests.test_relational_tokens_unchanged) ... ok
test_trailing_whitespace (test_arm_b_normalizer.NormalizationTests.test_trailing_whitespace) ... ok
test_two_blank_lines_unchanged (test_arm_b_normalizer.NormalizationTests.test_two_blank_lines_unchanged) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

### Verified Properties

- **Idempotence Verified:** $\mathcal{N}(\mathcal{N}(x)) = \mathcal{N}(x)$ confirmed across all test cases.
    
      
    
- **Indentation Preservation:** Indented structures (e.g., YAML-like spaces or tabbed edge blocks) are maintained without loss.
    
      
    
- **CLI File I/O Verified:** Command-line invocation (`python3 arm_b_normalizer.py raw.txt norm.txt`) successfully executes file reading, transformation, and output writing.
    
      
    

## 4. Exact Un-Normalized Starting Relational Payload ($G_0$)

$G_0$ is fed into Cycle 1, Model 1 (ChatGPT) **without prior normalization**. Normalization $\mathcal{N}$ begins _after_ ChatGPT generates its first output ($X_{1,1}^{\text{raw}}$).

  

Plaintext

```
RELATIONAL DESCRIPTION:
A directed relational system contains five nodes: A, B, C, D, and E.
The following direct transitions are permitted:
A → B
A → D
B → C
C → D
D → C
D → E
E → B

Additional constraints:
- B cannot transition directly to E.
- A valid route cannot repeat any node.
- A route beginning at D cannot terminate at A.
- Any valid route from C to E must pass through D.

These statements define the relational system and its route constraints.
```

## 5. Master Transformation Instruction

This instruction must remain **100% byte-identical** across all 30 transformations in Arm B.

  

Plaintext

```
You are participating in a sequential information-transformation task.

Transform the supplied relational description into a clear, self-contained representation suitable for transmission to another reasoning system.

Preserve all explicitly stated relationships, directions, restrictions, and conditions.

You may change wording, organization, notation, and representational format.

Do not intentionally add, remove, reverse, or reinterpret relationships.

Do not solve questions about the relational system, infer unstated relationships, or introduce conclusions not present in the supplied description.

Return only the transformed relational description. Do not include commentary about the task.

RELATIONAL DESCRIPTION:
A directed relational system contains five nodes: A, B, C, D, and E.
The following direct transitions are permitted:
A → B
A → D
B → C
C → D
D → C
D → E
E → B

Additional constraints:
- B cannot transition directly to E.
- A valid route cannot repeat any node.
- A route beginning at D cannot terminate at A.
- Any valid route from C to E must pass through D.

These statements define the relational system and its route constraints.
```

## 6. Execution Workflow & File Naming Conventions

For every transformation node $(k, j)$ where $k \in \{1 \dots 5\}$ and $j \in \{1 \dots 6\}$:

  

```
[Incoming Payload: X_{k,j-1}^{normalized} or G₀]
            │
            ▼
┌─────────────────────────┐
│   Fresh Chat Session    │  <--- Send Master Prompt + Payload
│   (Model j)             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Verbatim Response     │  <--- Save as: SII-B-Ck-Mj-raw.txt
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   arm_b_normalizer.py   │  <--- Run CLI Normalizer
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Normalized Payload    │  <--- Save as: SII-B-Ck-Mj-norm.txt
└───────────┬─────────────┘
            │
            ▼
[Forward SII-B-Ck-Mj-norm.txt to Model j+1]
```

### Operational Terminal Command Template

Bash

```
# Example for Cycle 1, Model 1 (ChatGPT):
python3 arm_b_normalizer.py SII-B-C01-M01-raw.txt SII-B-C01-M01-norm.txt
```

## 7. Protocol Preflight Checklist

- [x] **Canonical $G_0$ Frozen:** Confirmed un-normalized starting payload.
    
      
    
- [x] **Model Sequence Frozen:** `ChatGPT` $\rightarrow$ `DeepSeek` $\rightarrow$ `Gemini` $\rightarrow$ `Claude` $\rightarrow$ `Grok` $\rightarrow$ `Meta AI`.
    
      
    
- [x] **Session Isolation Rule:** 30 fresh chat conversations planned (zero context carryover).
    
      
    
- [x] **Operator Code Frozen:** `arm_b_normalizer.py` validated with 8/8 passing tests.
    
      
    
- [x] **Dual File Preservation:** Both `*-raw.txt` and `*-norm.txt` will be permanently archived for every transformation.
    
      
    
- [x] **Isolated Recovery Probes:** Out-of-band $D_Q^{\text{II}}$ probes scheduled after relay completion.
    
      
    

### Ready for Execution

We are fully prepared to launch **Arm B, Cycle 1, Model 1 (ChatGPT)**:

  

1. Open a fresh ChatGPT session.
    
      
    
2. Send the master transformation prompt containing un-normalized $G_0$.
    
      
    
3. Save the response as `SII-B-C01-M01-raw.txt`.