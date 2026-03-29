# Title

## Pre-watch questions
* what are rdds?
* what are they used for?

## Chunk 1
(only write concepts)
Distributed typed collections
JVM objects
highly optimized
partitioning
order of elements
order of operations
99 % DF


## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

### 3 main points
1. RDDs give you better control over your jobs however the tradeoff is they are harder to use and do not get the auto optimization that high level apis get.
2. Read: we can turn collections, files, or DataFrames into RDDs.
3. RDDs let you control the order or elements, the order of operations, more granular partition controls and storage controls for caching and checkpointing. However DF have select and join and optimization so 99% of time use DF.


### Plain english
* rdd gives more granular low level control to help boost performance if you know what you are doing. For 99% of time you should use DF. We can create RDD from file, dataframe, or collections.

## Chunk 1 compressed
Concept: RDD allows you to have low level control in job
Why it matters: Helps in rarer optimizations
Example: We have data that is not doing well with default optimizations so we use more granular control with rdd
One confusion: rdd and df let you repartition and persist but rdd has more lower level controls over it.
