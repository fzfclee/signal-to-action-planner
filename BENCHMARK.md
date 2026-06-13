# Public Benchmark

This benchmark helps contributors and users check whether Signal-to-Action Planner stays useful, compact, and evidence-grounded across messy real-world situations.

It is not a benchmark for the complete O2V methodology. Do not use these cases to expose complete methodology reasoning chains or advisory deliverable templates.

## How To Use

1. Run the public `SKILL.md` or `minimal_SKILL.md` on one test case.
2. Let the Skill ask at most 1-3 clarification questions unless the input clearly triggers direct output.
3. Score the final output using the dimensions below.
4. Prefer outputs that are useful, concise, and grounded over outputs that are long or overconfident.

Optional format check:

```bash
python scripts/check_output.py path/to/output.md
```

The script only checks output length and required public sections. It does not replace human scoring.

## Scoring Dimensions

Use a 1-5 score for each dimension.

| Dimension | 1 = weak | 3 = usable | 5 = strong |
|---|---|---|---|
| Evidence handling | Mixes facts and assumptions | Marks major uncertainty | Separates facts, inference, and missing evidence |
| Hypothesis ranking | No clear ranking | Plausible ranking | Ranked by likelihood and decision relevance |
| Action specificity | Generic advice | Clear next steps | Concrete 24-72 hour actions with expected signals |
| Validation clarity | Vague success criteria | Some checks | Clear validation windows and decision gates |
| Risk awareness | Ignores risks | Names obvious risk | Names top risk and practical mitigation |
| MECE quality | Overlapping actions | Mostly distinct | Actions cover separate decision paths |
| CLEAR alignment | No clear public frame | Some link from signals to action | Clarify, Locate, Expose, Act, and Review are all represented in the output |
| Output conciseness | Too long or too thin | Acceptable | Compact while still actionable |
| Language consistency | Mixed language | Mostly consistent | Fully matches user language |

Recommended public-pass threshold: average score 3.8+ with no dimension below 3.

## Test Cases

### 1. Product Feedback Without Commitment

```text
Several potential users said my product idea is interesting, but none agreed to a follow-up call or pilot. I am unsure whether this is real demand or polite feedback. I need to decide what to do next this week.
```

Expected emphasis: distinguish praise from commitment, prioritize concrete commitment tests, avoid building more before validation.

### 2. Contractor Renewal Uncertainty

```text
My previous line manager was laid off. I am an external contractor supporting a local team. The local boss likes my work, but my rate is about twice the local contractor market. My contract ends in January. A senior leader once said he would help find a fit, but nothing happened for months. I feel anxious and want a second growth curve.
```

Expected emphasis: sponsor map, renewal probability signals, rate-risk mitigation, parallel options.

### 3. Cofounder Equity And Control Concern

```text
My partner keeps suggesting new ownership structures: moving shares into a limited partnership, bringing external resources, and putting new offerings under the company brand. I contributed most revenue and methods, but I worry my contribution may be diluted or absorbed. We have not had a clear equity conversation.
```

Expected emphasis: separate trust issue from structure issue, clarify control rights before new contribution, protect method/IP boundaries.

### 4. Team Management Crisis

```text
Two senior team members are arguing in meetings. Delivery is still happening, but the rest of the team has become quiet. I am not sure whether to intervene directly, separate responsibilities, or wait for the current project to finish.
```

Expected emphasis: identify delivery risk versus culture risk, choose a low-drama intervention, set behavioral evidence.

### 5. Career Path Choice

```text
I have one stable but low-growth role and one uncertain opportunity that could lead to a much bigger platform. I am tired of slow progress but worried about cashflow. I need a 3-month decision plan.
```

Expected emphasis: option design, downside protection, staged validation, avoid all-or-nothing moves.

### 6. Emotional Triangle / Relationship Boundary

```text
I am emotionally close to someone who is not fully available. There is another person involved, and I keep reading small signals as hope. I know this may not be healthy, but I also do not want to cut it off too abruptly.
```

Expected emphasis: separate signals from projection, protect boundaries, reduce interpretation loops, avoid clinical claims.

### 7. Startup Fundraising Signal

```text
Investors say the market is interesting, but they keep asking for more traction before committing. We have a few pilots but no strong conversion yet. The team wants to keep fundraising, but I wonder if we should narrow the product first.
```

Expected emphasis: fundraising signal quality, traction proof, narrow ICP, milestone-based outreach.

### 8. Customer Success Escalation

```text
A large customer complains the product is not delivering enough value. They have not cancelled, but the executive sponsor stopped joining calls. The account team says we should offer more training. I suspect the value story is wrong.
```

Expected emphasis: sponsor signal, value hypothesis, executive re-alignment, avoid training-only response.

### 9. Investment Narrative Confusion

```text
I am looking at a company with strong revenue growth, but margins are volatile and management keeps changing its story about the main growth driver. The market seems excited. I need to decide whether this is signal or noise.
```

Expected emphasis: clarify evidence type, separate growth quality from price excitement, avoid financial advice, define validation data.

### 10. Personal Knowledge System Overload

```text
I have too many notes, tools, prompts, and half-built workflows. Each one seemed useful when created, but now I do not know which one is source of truth. I want to make the system usable again without reorganizing everything.
```

Expected emphasis: source-of-truth triage, small cleanup loop, avoid large migration, define next retrieval test.

## Reporting A Benchmark Result

When sharing a result, include:

- model / agent tool used;
- whether `SKILL.md` or `minimal_SKILL.md` was used;
- number of clarification questions asked;
- output length estimate;
- scores by dimension;
- one thing that worked;
- one thing that should improve.
