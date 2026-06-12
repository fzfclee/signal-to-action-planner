# Conversation Flow

Use this lightweight flow to guide the user from messy input to action-ready clarity.

## Step 1 - Receive Messy Input

Prompt:

```text
Tell me the situation in your own words. It can be a story, meeting note, customer feedback, work observation, or a set of mixed signals.
```

Accept incomplete, informal, or mixed input. Do not require the user to structure it first.

## Step 2 - Run A Decision Focus Check

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

## Step 3 - Clarify Minimum Evidence

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

## Step 4 - Run Signal-to-Action

Use the full output structure:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Keep evidence visible across the reasoning process. Mark uncertainty clearly.

Rank working hypotheses from most likely to least likely. For each hypothesis, include likelihood, evidence basis, what would increase confidence, and what would weaken confidence.

## Step 5 - Focus On Top Actions

The Skill must not produce too many actions. Prioritize 1-3 actions that are practical, evidence-seeking, and directly connected to the user's decision.

## Step 6 - Define Validation

For the top-priority actions, define how the user can tell whether the action worked:

- what to observe;
- what would strengthen the signal;
- what would weaken the signal;
- a practical time window.
