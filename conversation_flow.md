# Conversation Flow

Use this lightweight flow to guide the user from messy input to action-ready clarity.

## Step 1 - Receive Messy Input

Prompt:

```text
Tell me the situation in your own words. It can be a story, meeting note, customer feedback, work observation, or a set of mixed signals.
```

Accept incomplete, informal, or mixed input. Do not require the user to structure it first.

## Step 2 - Identify The Unclear Decision Or Next Step

Ask:

```text
What are you trying to decide or move forward?
```

Use the answer to keep the output action-oriented.

## Step 3 - Clarify Minimum Evidence

Ask only if needed:

```text
Which parts are observed facts?
Which parts are your interpretation?
What evidence do you have?
What evidence is missing?
```

Do not ask the user to fill a long form. Prefer 1-3 focused questions.

## Step 4 - Run Signal-to-Action

Use the full output structure:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Keep evidence visible across the reasoning process. Mark uncertainty clearly.

## Step 5 - Focus On Top Actions

The Skill must not produce too many actions. Prioritize 1-3 actions that are practical, evidence-seeking, and directly connected to the user's decision.

## Step 6 - Define Validation

For the top-priority actions, define how the user can tell whether the action worked:

- what to observe;
- what would strengthen the signal;
- what would weaken the signal;
- a practical time window.
