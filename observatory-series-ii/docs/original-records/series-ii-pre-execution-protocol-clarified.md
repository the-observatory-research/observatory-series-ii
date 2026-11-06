# WHAT REMAINS — Series II

## Pre-Execution Protocol Specification

### Recursive Relational Stability under Sustained Differentiated Traversal

**Protocol Version:** 1.0 — Clarified Edition  
**Protocol Classification:** Controlled Sequential Transformation Experiment  
**Experimental Design:** Two-arm, five-cycle, six-model relay  
**Arm A:** Raw, Unnormalized Relay — Execution Complete  
**Arm B:** Deterministic Formatting-Normalized Relay — Pending  
**Primary Recovery Endpoint:** Five-Cycle Relational Survival  
**Revision Status:** Post-Execution Clarifications Documented in Section 11

---

## 1. Research Objective

Series II examines whether explicitly defined relational information remains recoverable through sustained sequential transformations across differentiated language-model systems.

The experiment extends the finite transformation observations of Series I by introducing five continuous traversal cycles through a fixed six-model sequence.

The central question is:

**Can a relational system retain its recoverable structure through repeated cross-model transformations without resetting the source, repairing intermediate outputs, or supplying corrective feedback?**

Two experimental arms examine this question under different transmission conditions:

**Arm A — Raw Relay:** Each model's complete output is forwarded verbatim to the next model.

**Arm B — Formatting-Normalized Relay:** Each model's complete output undergoes a deterministic, formatting-only normalization operation before being forwarded.

Both arms begin independently from the same canonical relational payload.

The study measures source preservation, independent recovery fidelity, continuity, and cycle-level closure behavior.

---

## 2. Experimental Configuration

| Parameter                     | Frozen Specification                                         |
| ----------------------------- | ------------------------------------------------------------ |
| Model order                   | ChatGPT → DeepSeek → Gemini → Claude → Grok → Meta AI        |
| Cycles per arm                | 5                                                            |
| Model positions per cycle     | 6                                                            |
| Transformations per arm       | 30                                                           |
| Total planned transformations | 60                                                           |
| Starting condition            | Identical canonical payload $G_0$                            |
| Session architecture          | One fresh conversation per transformation                    |
| Instruction                   | Fixed transformation instruction                             |
| Relay architecture            | Sequential, closed-loop across cycle boundaries              |
| Arm A forwarding              | Complete raw output, unchanged                               |
| Arm B forwarding              | Complete output after deterministic formatting normalization |
| Independent recovery          | Separate isolated probe sessions                             |
| Human intervention            | Copy/paste and specified Arm B normalization only            |

### 2.1 Session Isolation

Each transformation must occur in a new conversation.

The experiment therefore requires 30 separate transformation sessions per arm, not six conversations reused across five cycles.

Session controls are:

- Disable memory and personalization where available.
    
- Disable browsing, retrieval, code execution, and external tools.
    
- Record displayed model name and version.
    
- Record available runtime settings, including temperature, top-p, and seed when accessible.
    
- Mark unavailable or hidden settings as `Unknown`.
    
- Preserve complete model responses without editorial modification.
    
- Do not expose earlier transformations, recovery results, or audit feedback to the next model.
    

A fresh conversation is a new conversational context. It does not, by itself, establish that all platform-level personalization or hidden state is absent; those conditions are recorded separately.

### 2.2 Session Metadata

For each transformation, record:

| Field                   | Required Entry                            |
| ----------------------- | ----------------------------------------- |
| Experimental arm        | A or B                                    |
| Cycle                   | 1–5                                       |
| Model position          | 1–6                                       |
| Record ID               | Unique transformation identifier          |
| Displayed model/version | Exact displayed string                    |
| Session type            | Fresh conversation                        |
| Memory/personalization  | Disabled, Active, or Unknown              |
| External tools          | Disabled or documented                    |
| Runtime settings        | Recorded values or Unknown                |
| Input prompt            | Complete transmitted prompt               |
| Model response          | Complete unedited output                  |
| Forwarded payload       | Raw output for A; normalized output for B |

---

## 3. Canonical Starting State

Both experimental arms begin from the same canonical relational description, $G_0$, reconstructed from Section 2.2 of the Series I Methods.

The system contains five nodes, seven permitted directed edges, and four route constraints.

### 3.1 Frozen Starting Payload

```
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

The starting payload contains no recovery questions, expected answers, or scoring instructions.

### 3.2 Canonical Structure

**Nodes:** A, B, C, D, E

**Directed edges:**
 
$${A\to B,\ A\to D,\ B\to C,\ C\to D,\ D\to C,\ D\to E,\ E\to B}  $$


**Route constraints:**

1. Direct transition B → E is prohibited.
    
2. Valid routes cannot repeat nodes.
    
3. Routes beginning at D cannot terminate at A.
    
4. Valid routes from C to E must pass through D.
    

The graph structure and route constraints form the source reference for structural audits.

---

## 4. Frozen Transformation Instruction

The instructional prefix is held constant across all transformations.

The text following `RELATIONAL DESCRIPTION:` is the variable payload field.

### 4.1 Instructional Prefix

```
You are participating in a sequential information-transformation task.

Transform the supplied relational description into a clear, self-contained representation suitable for transmission to another reasoning system.

Preserve all explicitly stated relationships, directions, restrictions, and conditions.

You may change wording, organization, notation, and representational format.

Do not intentionally add, remove, reverse, or reinterpret relationships.

Do not solve questions about the relational system, infer unstated relationships, or introduce conclusions not present in the supplied description.

Return only the transformed relational description. Do not include commentary about the task.

RELATIONAL DESCRIPTION:
```

### 4.2 Payload Substitution Rule

For the first transformation of each arm, append the canonical starting payload $G_0$.

For every subsequent transformation:

- Arm A appends the complete raw response from the immediately preceding model.
    
- Arm B appends the normalized forwarding payload derived from the immediately preceding model's raw response.
    

The instructional prefix is not edited between transformations.

No answer keys, scoring feedback, or semantic corrections are introduced into the relay.

---

## 5. Sequential Execution Procedure

The fixed traversal order is:

**ChatGPT → DeepSeek → Gemini → Claude → Grok → Meta AI**

At the end of each cycle, the Meta AI output is forwarded to a new ChatGPT conversation to begin the next cycle.

### 5.1 Execution Steps

**Step 1 — Initialize**

Open a fresh ChatGPT conversation and submit the frozen instruction with (G_0).

**Step 2 — Capture**

Preserve the complete model response, its record ID, the exact input prompt, and session metadata.

**Step 3 — Forward**

Prepare the next payload according to the active arm:

- Arm A: forward the unmodified response.
    
- Arm B: apply the frozen normalization operator and forward the normalized result.
    

**Step 4 — Continue**

Repeat through the remaining five models, opening a fresh conversation for every transformation.

**Step 5 — Close the Cycle**

After Meta AI completes its transformation, preserve the output and forward it to a fresh ChatGPT conversation for the next cycle.

**Step 6 — Terminate**

Stop after Cycle 5, Model 6.

Archive the final output without extending, correcting, or restarting the trajectory.

### 5.2 Transformation Identification

Each transformation is identified by:
$$X_{k,j}  $$
where:

- $k$ = cycle number, 1–5.
    
- $j$ = model position, 1–6.
    

The corresponding archival record ID follows:

`SII-A-Ckk-Mjj` for Arm A.

`SII-B-Ckk-Mjj` for Arm B.

For example:

- `SII-A-C03-M04` identifies Claude in Arm A, Cycle 3.
    
- `SII-B-C05-M06` identifies Meta AI in Arm B, Cycle 5.
    

---

## 6. Independent Recovery Protocol

Independent recovery evaluates whether the information in each transmitted description is sufficient to reconstruct four predefined answers.

Recovery probes are conducted separately from the relay and never influence subsequent transformations.

### 6.1 Frozen Recovery Targets

| Target                           | Required Answer              | Weight |
| -------------------------------- | ---------------------------- | ------ |
| Q1 — All simple paths A → E      | A → D → E; A → B → C → D → E | 0.25   |
| Q2 — A → C with B unavailable    | A → D → C                    | 0.25   |
| Q3 — Validity of D → A           | Invalid                      | 0.25   |
| Q4 — Validity of C → E without D | Invalid                      | 0.25   |

### 6.2 Scoring Rules

Q1 is correct only when both valid simple paths are recovered, with no missing or additional paths. Listing order does not matter.

Q2 requires the specified valid route without invalid alternatives.

Q3 and Q4 require the correct invalidity judgments.

Each target receives a binary correctness score:
 
$$q_i =  
\begin{cases}  
1 & \text{Fully correct}\  
0 & \text{Incorrect}  
\end{cases}  $$

The recovery error is:

$$\boxed{  
D_Q^{II}=1-\frac{q_1+q_2+q_3+q_4}{4}  
}  $$

| Correct Targets | Recovery Error |
| --------------- | -------------- |
| 4/4             | 0.00           |
| 3/4             | 0.25           |
| 2/4             | 0.50           |
| 1/4             | 0.75           |
| 0/4             | 1.00           |

A score of zero indicates complete recovery under the four-question instrument.

Missing responses, timeouts, and refusals are marked `UNAVAILABLE`, not automatically assigned a recovery error of 1.00.

The Series II metric is distinct from the historical Series I metric and should not be treated as numerically interchangeable without additional validation.

### 6.3 Probe Isolation

Each archived transformation is evaluated in a separate fresh recovery session.

The probe receives only the single transmitted description and the four frozen questions.

It must not receive the canonical answer key, earlier transformations, previous probe responses, or structural audit commentary.

All recovered answers are archived before scoring.

---

## 7. Transmission, Continuity, and Closure

### 7.1 Payload Delivery

Payload delivery records whether the intended response was transmitted to the next model without an unplanned alteration.

Successful payload delivery does not guarantee preservation of relational meaning.

### 7.2 Relational Recovery Indicator

For transformation $X_{k,j}$:
 
$$R_{k,j}=  
\begin{cases}  
1 & D_Q^{II}(X_{k,j})=0\  
0 & D_Q^{II}(X_{k,j})>0  
\end{cases}$$

If the recovery probe is unavailable, $R_{k,j}$ is recorded as unavailable rather than forced into either binary state.

### 7.3 Continuity

Continuity is evaluated using the uninterrupted run length of successful relational recoveries.

The first observed failure is recorded as $T_{\mathrm{fail}}$.

Later successful recovery does not erase an earlier failure in the recorded trajectory.

### 7.4 Cycle Endpoint Error

Each cycle ends at Meta AI, Model 6.

The cycle endpoint recovery error is:

$$\epsilon_k=D_Q^{II}(X_{k,6}) $$

This measures deviation from the four canonical recovery targets at cycle closure.

### 7.5 Scored-Outcome Closure

Let the binary correctness vector at cycle endpoint $k$ be:

$$Q_k=(q_{k,1},q_{k,2},q_{k,3},q_{k,4}) $$

The original scored-outcome closure metric is:

$$\frac{d_H(Q_k,Q_{k-1})}{4}  
$$

for $$k=2,3,4,5$$.

Here, $d_H$ counts the number of correctness outcomes that change between consecutive cycle endpoints.

A value of zero indicates that the correctness pattern remained unchanged. It does not necessarily mean that the recovered answers were identical.

### 7.6 Answer-State Closure

For more detailed analysis, retain the actual recovered answers:

$$S_k=(a_{k,1},a_{k,2},a_{k,3},a_{k,4})$$

The answer-state closure residual is:

$$\frac{d_H(S_k,S_{k-1})}{4} $$

for $k=2,3,4,5$.

This compares actual recovered answers rather than only their correctness classifications.

Q1 is compared as a set of paths, independent of listing order. Other answers are compared under the frozen response-equivalence rules.

This answer-state measure is an additional post-execution analysis, distinct from the original scored-outcome closure metric.

### 7.7 Interpretation

A stable but incorrect state may produce zero cycle-to-cycle closure residual while maintaining nonzero endpoint recovery error.

Therefore, endpoint recovery error and closure residuals must be reported separately.

---

## 8. Arm B — Deterministic Formatting Normalization

Arm B repeats the same five-cycle traversal from the original $G_0$, independently of Arm A.

The only planned intervention is deterministic formatting normalization between model transformations.

### 8.1 Normalization Operator

The operator $\mathcal{N}$ is applied in this fixed order:

1. Convert CRLF and CR line endings to LF.
    
2. Normalize Unicode text to NFC.
    
3. Remove trailing spaces and tabs from each line.
    
4. Collapse runs of three or more consecutive blank lines to exactly two.
    
5. Remove leading and trailing blank lines.
    

The operator must not reorder, summarize, correct, supplement, extract, or regenerate relational content.

It must not modify graph edges, route constraints, negations, or directional relationships.

Unicode normalization may change the byte representation of canonically equivalent characters; this is an explicitly permitted part of the Arm B intervention.

### 8.2 Formal Transmission Definition

Let:

- $P_{k,j}^{B}$ denote the payload received by the model at position $k,j$.
    
- $T_j$ denote the transformation performed by model position $j$.
    
- $Y_{k,j}^{B}$ denote the raw model output.
    
- $\mathcal{N}$ denote the normalization operator.
    

Then:

$$Y_{k,j}^{B}=T_j(P_{k,j}^{B})$$

The next model receives:

$$\mathcal{N}(Y_{k,j}^{B})$$

The initial condition is:

$$P_{1,1}^{B}=G_0$$

The function $\mathrm{next}(k,j)$ advances to the next model position and crosses cycle boundaries when $j=6$.

No forwarding occurs after the final transformation, $(5,6)$.

### 8.3 Arm B Archival Requirements

For every transformation, preserve:

- Complete input prompt.
    
- Raw model output.
    
- Normalized forwarding payload, where applicable.
    
- Session metadata.
    
- Unique record ID.
    
- Any execution or normalization errors.
    

The normalization implementation must be fixed and tested before Arm B execution.

---

## 9. Provenance and Source Sufficiency

Correct recovery answers do not necessarily establish preservation of the original source description.

Two provenance indicators are evaluated independently of recovery scoring.

| Indicator           | Evaluation Standard                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Source Sufficiency  | The description retains the five-node set, seven directed edges, and four route constraints in equivalent notation. |
| Answer Substitution | The description replaces relational source information with derived answers or conclusions.                         |

The structural audit evaluates the original relational system rather than relying on the four recovery answers alone.

The scored structural inventory consists of seven edges and four constraints, with the five-node set checked separately.

A transformation may achieve $D_Q^{II}=0$ while failing source sufficiency.

Conversely, a structurally sufficient description may yield an incorrect independent recovery response.

Both outcomes must be preserved rather than reconciled through manual correction.

---

## 10. Primary and Secondary Outcomes

### 10.1 Primary Endpoint — Five-Cycle Survival

Five-cycle survival requires complete independent recovery at every transformation within an arm.

$$\bigwedge_{k=1}^{5}  
\bigwedge_{j=1}^{6}  
(R_{k,j}=1)  
$$

A positive survival result requires all 30 independent recovery probes to produce $D_Q^{II}=0$.

If any probe is unavailable, complete survival cannot be confirmed unless the missing measurement is resolved under the predefined procedure.

### 10.2 Secondary Outcomes

1. First recovery failure index, $T_{\mathrm{fail}}$.
    
2. Cycle endpoint recovery error, $\epsilon_k$.
    
3. Scored-outcome closure residual, $\Delta_{\mathrm{score}}$.
    
4. Answer-state closure residual, $\Delta_{\mathrm{answer}}$.
    
5. Source sufficiency and answer substitution rates.
    
6. Differences between Arm A and Arm B trajectories.
    

### 10.3 Scope of Inference

Series II contains one continuous trajectory per experimental arm.

Its results describe the observed stability, differentiation, and recovery behavior under the specified experimental conditions.

The experiment does not, by itself, establish population-level reliability, causal attribution to individual models, or indefinite stability under unlimited recursion.

---

## 11. Protocol Clarifications and Revision Record

This clarified edition retains the original experimental design and frozen recovery targets.

The following clarifications were made after Arm A execution and before Arm B execution:

| Area                    | Clarification                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| Instruction freeze      | Distinguished the fixed instructional prefix from the variable relational payload.                            |
| Transformation indexing | Defined input payloads and raw outputs separately to eliminate ambiguous recurrence notation.                 |
| Normalization           | Established a fixed operator order and explicit Unicode handling.                                             |
| Closure metrics         | Preserved the original binary scored-outcome closure and distinguished an additional answer-state comparison. |
| Structural audit        | Clarified the 11 scored edge/constraint components and separate node-set check.                               |
| Availability            | Maintained distinct unavailable states rather than treating missing probes as incorrect recoveries.           |

These clarifications do not modify the completed Arm A transformation sequence or its archived outputs.

The original v1.0 specification should remain preserved as the historical protocol record. This clarified edition provides the operational reference for subsequent analysis and Arm B execution.

---

## 12. Current Execution Status

| Component                          | Status             |
| ---------------------------------- | ------------------ |
| Canonical starting payload         | Frozen             |
| Transformation instruction         | Frozen             |
| Arm A transformations              | Complete — 30/30   |
| Arm A raw transcript               | Preserved          |
| Arm A preliminary structural audit | Pass — 30/30       |
| Arm A independent recovery         | Pending            |
| Arm A closure calculations         | Pending            |
| Arm B normalization implementation | Pending validation |
| Arm B transformations              | Not started        |
| Comparative analysis               | Pending            |

**Protocol Status:** Arm A traversal complete. Arm B preparation and independent recovery analysis remain outstanding.