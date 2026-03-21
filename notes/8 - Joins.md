
# Title

## Pre-watch questions
* What are joins?
* how are they done in spark?
* what is performance?
* what different types do they support, and difference between types?

## Chunk 1
(only write concepts)
wide transformation
join data
discareded
left join
right join
outer join
left outer
right outer
left semi
right semi
left anti join
right anti join


dealing with columns after joins
## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

# 3 main points
1. JOins let us combine data from seperate dataframes into one.
2. Joins are expensive since they are a wide transformation. Meaning data gets shuffled.
3. There are many different types of joins from left/right/inner/outer/semi/anti

# plain english
Joins combine data from diff dataframes into one. They are **wide** transformations meaning that data gets moved across nodes.\

diff types
**inner** - take rows that are in left and in right dataframe that join key appears in both.
**left or left-outer** - inner join + all rows from left, so will have nulls (in columns of right table) in rows where entry in left table that had no entries in right
**right or right-outer** - same as left but for right df
**outer** - all rows from both sides
**left-semi** - show rows in left table that have entries in right, but do not actually join with right data.
**left-anti** - ONly rows from left table that do not have a match on right table

# why it matters
we can consume multiple large datasets and join them in order to answer questions with more columns.

# one example
Imagine we need to rank prime video titles that user watched however in watch history we dont have title metadata so we need to join



## Chunk 1 compressed
Concept: Joins help us combine datasets
Why it matters: Hydrate data with metadata from other tables
Example: Imagine we need to rank prime video titles that user watched however in watch history we dont have title metadata so we need to join
One confusion: ...
