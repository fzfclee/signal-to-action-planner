# Conversation Flow

Use this lightweight flow to guide the user from messy input to action-ready clarity.

Use one language consistently. Match the user's dominant language or the language required by the user's system / project instructions. Keep headings, option labels, explanations, actions, validation, and action roadmap in that language unless quoting user-provided terms or proper nouns. In Chinese, call the roadmap `行动路线`.

If this Skill has been updated, follow the current `SKILL.md` and this flow strictly. Do not rely on prior memory, old test behavior, or earlier conversation patterns when they conflict with the current version.

On tools with memory or cached skills, apply the current `SKILL.md` at the start of each run. If the tool may be using an older cached version, refresh or reload before asking the first question.

Keep user-facing intermediate reasoning concise by default. Use the chain to think clearly, but do not show every reasoning step in detail unless the user explicitly requests detailed reasoning, such as with `--detailed` or a similar instruction.

Keep default visible output under 6,000 UTF-8 bytes. If the output may be too long, compress automatically and preserve priorities, validation, and action roadmap first.

## Step 1 - Receive Messy Input

Prompt:

```text
Tell me the situation in your own words. It can be a story, meeting note, customer feedback, work observation, or a set of mixed signals.
```

Accept incomplete, informal, or mixed input. Do not require the user to structure it first.

If the input is too long for the platform, ask for the most decision-relevant excerpt, the current decision, or a smaller chunk. Do not try to process an oversized document in one pass.

Do not jump from messy input directly to the 7-section output unless the user explicitly asks to skip questions or continue to output. The default experience must include front-end interaction.

## Step 2 - Run A Decision Focus Check

Do not ask the user to choose output detail level at the start. Use concise output by default unless the user explicitly requests detailed reasoning.

Before producing the full output, check whether the user's desired decision, priority, or success criterion is clear. For messy situations with several possible directions, ask one lightweight choice question first.

Use a tailored multiple-choice question with 2-4 short options plus one free-text option. Example:

```text
To make the action plan useful, what decision do you most want to clarify first?

A. How likely the current path is to continue.
B. What evidence to collect before acting.
C. Which next action has the best risk/reward.
D. Other / more context: ...
```

If the user explicitly asks for direct output, do not force a question. Otherwise, ask the decision focus check even when the user's story looks detailed, because the intended optimization may still be unclear.

## Step 3 - Run A Dynamic Intake Loop

After the decision focus is clear, ask one relevant intake question at a time if the answer would improve accuracy. Do not ask 3-5 questions in one message.

Use this format:

```text
To make the roadmap more accurate, I will ask one question at a time. You can choose skip / not sure or say "continue".

Question [number]:
[Question tailored to the user's latest answer and remaining uncertainty]

A. [Short option]
B. [Short option]
C. [Short option]
D. Skip / not sure.
E. Other / more context: ...
```

Keep the loop short:

- Ask one question per message.
- Choose the next question based on the user's latest answer.
- Aim for 3 questions for simple cases.
- 4-5 questions only when uncertainty is high.
- Every question must include a skip / not sure option.
- The user can say "continue" at any time.
- Do not make the user fill a long form.

## Step 4 - Clarify Minimum Evidence

Ask only if needed. Do not use a fixed list of questions. Decide what to ask by checking which part of the chain is too weak to continue:

- Fact gap: the input does not distinguish observation from interpretation.
- Signal gap: the input contains many details but no clear signal.
- Implication gap: the signal exists but its meaning is ambiguous.
- Hypothesis gap: there is no testable explanation.
- Action gap: the user has too many possible actions.
- Validation gap: there is no way to tell whether the action worked.

Generate 1 focused question from the actual situation when possible. If more context is truly required, use the dynamic intake loop rather than asking a multi-question form.

Prefer a multiple-choice style with 2-4 short options plus one optional free-text answer. This keeps the interaction easy while still allowing the user to add nuance.

Example:

```text
To identify the weakest part of the chain, which gap matters most right now?

A. I am not sure what the real facts are.
B. I know the facts, but I am not sure what signal they create.
C. I see the signal, but I am not sure what action to take.
D. Other / more context: ...
```

Adapt these shapes to the user's wording. Do not ask the user to fill a long form. Prefer one focused question when one is enough.

After the user answers, reassess the chain. Ask another question only if it changes the action or validation plan. Otherwise continue to the output.

## Step 5 - Use Mid-Process Checkpoints

Do not limit interaction to the first question. After identifying evidence, signals, implications, or hypotheses, ask another lightweight question if the intermediate result creates a real fork.

Use checkpoints such as:

- Evidence checkpoint: ask for missing evidence if the likelihood ranking is unstable.
- Hypothesis checkpoint: ask which hypothesis best matches the user's lived reality if two are close.
- Action roadmap checkpoint: ask which constraint matters most if actions compete.

Keep each checkpoint as a short multiple-choice question with 2-4 options plus one free-text option.

## Step 6 - Run Signal-to-Action

Use the compressed output structure:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Keep evidence visible, but merge facts, fact evidence strength, and key signals into one compact user-facing section.

Separate fact evidence strength from inference confidence. If a user directly reports an observation, experience, number, or conversation, treat that as evidence for the reported fact. If the strategic meaning remains uncertain, keep the fact evidence strong and lower only the implication, hypothesis, or action confidence.

Compress implications and hypotheses into conclusion-level output. Rank working hypotheses from most likely to least likely. Expand confidence-increasing and confidence-weakening details only for the most important or most uncertain hypothesis, or when the user explicitly requests detailed reasoning.

## Step 7 - Focus On Top Actions

The Skill must not produce too many actions. Prioritize 1-3 MECE actions that are practical, evidence-seeking, and directly connected to the user's decision. Make the order explicit:

- Priority 1: do first.
- Priority 2: do next.
- Priority 3: do after that, if still needed.

Keep action descriptions separate from validation. Actions say what to do and why; validation says how to judge whether the action worked.

## Step 8 - Define Validation

For the top-priority actions, define how the user can tell whether the action worked:

- what to observe;
- what would strengthen the signal;
- what would weaken the signal;
- a practical time window.

## Step 9 - Give An Action Roadmap

End with a short action roadmap. Localize the heading, for example `行动路线` in Chinese.

- First: the highest-priority action.
- Next: the second action.
- Then: the third action or contingency.
- Decision point: what evidence should change the user's direction.

Keep the action roadmap separate from validation. The roadmap is about sequence and decision gates, not a repeat of the validation plan.
