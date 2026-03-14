# Spark Video Retention Algorithm

## Goal
Process one video lecture in a way that maximizes retention instead of passive familiarity.

## Inputs
- `video`
- `notebook`
- `timer`
- `optional_practice_env`

## Output
- `core_concepts_remembered`
- `confusions_identified`
- `1_small_application_completed`

---

## Global Rules
1. Do **not** watch passively from start to finish.
2. Do **not** transcribe everything.
3. Pause every `5-10 minutes` or at every major concept boundary.
4. After each pause, recall from memory **before** checking notes or rewatching.
5. At the end, produce a short summary from memory.
6. Review again later the same day and the next day.

---

## Data Structures

### Notes Template
For each concept, store:
- `Concept`
- `Why it matters`
- `Example`
- `One confusion`

### Recall Template
For each chunk, answer from memory:
- `What were the 3 main points?`
- `What is the idea in plain English?`
- `Why does it matter in Spark?`
- `What is one example?`

---

## Procedure

### Step 0: Initialize
1. Open `video`.
2. Open `notebook`.
3. Set `timer`.
4. Create section in notes called `Pre-watch questions`.

### Step 1: Pre-watch activation
1. Before pressing play, write `2-3` questions you want answered.
2. Example questions:
    - `What problem is this Spark topic solving?`
    - `What are the important tradeoffs?`
    - `What would make this slow or expensive?`

### Step 2: Watch first chunk
1. Play `5-10 minutes` of the video.
2. While watching, only capture:
    - concept names
    - short phrases
    - diagrams
    - examples
3. Do **not** attempt full sentences unless absolutely necessary.

### Step 3: Pause and retrieve
1. Pause the video.
2. Hide the screen or look away.
3. From memory, write:
    - the `3 main points`
    - the `plain English explanation`
    - `why it matters`
    - `one example`
4. Only after recall, look back and fill gaps.

### Step 4: Compress notes
1. Convert the chunk into this format:

```text
Concept: ...
Why it matters: ...
Example: ...
One confusion: ...
