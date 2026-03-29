# Title

## Pre-watch questions
* how to parition with rdds?
* how to do transformations?

## Chunk 1
(only write concepts)


## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

### 3 main points
1. coalese reduces number of partitions but it is NOT A FULL SHUFFLE at the cost of not having data evenly distributed on partitions. Repartition does redistribute however it does so evenly and it is a SHUFFLE.
2. we can do transformations on rdds with functions such as .map .filter .groupBy.
3. We can do actions on rdds with functions like .reduce, .count, .min, .max. min is not an action on DF but is on RDD.

### Plain English
RDDs allow us to do similar transfomrations as DF mostly through .map, .filter, .groupBy. WE can also control partitions through repartition and coalese

## Chunk 1 compressed
Concept: rdds allow us to do similar transformations as Dataframes
Why it matters: we can do similar actions but lower level of control
Example: example is iterate through all amazon products and find average rating by category 
One confusion: coalese does not involve full shuffle but repartition does, however coalese does move data between nodes.
