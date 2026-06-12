# Conversation Flow

Use this lightweight flow to guide the user from messy input to action-ready clarity.

Use one language consistently. Match the user's dominant language or the language required by the user's system / project instructions. Keep headings, option labels, explanations, actions, validation, and roadmap in that language unless quoting user-provided terms or proper nouns.

Keep user-facing intermediate reasoning concise by default. Use the chain to think clearly, but do not show every reasoning step in detail unless the user chooses detailed reasoning or asks for it later.

## Step 1 - Receive Messy Input

Prompt:

```text
Tell me the situation in your own words. It can be a story, meeting note, customer feedback, work observation, or a set of mixed signals.
```

Accept incomplete, informal, or mixed input. Do not require the user to structure it first.

## Step 2 - Run A Detail Level Check

Ask whether the user wants detailed reasoning shown. Default to concise output.

Use a lightweight choice question:

```text
Do you want me to show the detailed reasoning process?

A. No, keep the reasoning concise and focus on actions. (Default)
B. Yes, show the key reasoning steps.
C. Only show details when something is uncertain.
D. Other / more context: ...
```

If the user does not answer but continues with the situation, use option A by default.

## Step 3 - Run A Decision Focus Check

Before producing the full output, check whether the user's desired decision, priority, or success criterion is clear. For messy situations with several possible directions, ask one lightweight choice question first.

Use a tailored multiple-choice question with 2-4 short options plus one free-text option. Example:

```text
To make the action plan useful, what decision do you most want to clarify first?

A. How likely the current path is to continue.
B. What evidence to collect before acting.
C. Which next action has the best risk/reward.
D. Other / more context: ...
```

If the user has already made the decision focus clear, skip this step and continue. If the user explicitly asks for direct output, do not force a question.

## Step 4 - Clarify Minimum Evidence

Ask only if needed. Do not use a fixed list of questions. Decide what to ask by checking which part of the chain is too weak to continue:

- Fact gap: the input does not distinguish observation from interpretation.
- Signal gap: the input contains many details but no clear signal.
- Implication gap: the signal exists but its meaning is ambiguous.
- Hypothesis gap: there is no testable explanation.
- Action gap: the user has too many possible actions.
- Validation gap: there is no way to tell whether the action worked.

Generate 1 focused question from the actual situation when possible. If more context is truly required, ask no more than 3 questions at once.

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
- Roadmap checkpoint: ask which constraint matters most if actions compete.

Keep each checkpoint as a short multiple-choice question with 2-4 options plus one free-text option.

## Step 6 - Run Signal-to-Action

Use the full output structure:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Keep evidence visible across the reasoning process, but summarize it compactly for the user. Mark uncertainty clearly.

Rank working hypotheses from most likely to least likely. For each hypothesis, include likelihood and the shortest useful evidence basis. Add confidence-increasing and confidence-weakening details when they change the action plan, when uncertainty is high, or when the user chooses detailed reasoning.

## Step 7 - Focus On Top Actions

The Skill must not produce too many actions. Prioritize 1-3 actions that are practical, evidence-seeking, and directly connected to the user's decision. Make the order explicit:

- Priority 1: do first.
- Priority 2: do next.
- Priority 3: do after that, if still needed.

For each priority action, include its own validation method.

## Step 8 - Define Validation

For the top-priority actions, define how the user can tell whether the action worked:

- what to observe;
- what would strengthen the signal;
- what would weaken the signal;
- a practical time window.

## Step 9 - Give A Roadmap

End with a short roadmap:

- First: the highest-priority action and its validation.
- Next: the second action and its validation.
- Then: the third action or contingency.
- Decision point: what evidence should change the user's direction.
