
# Title

## Pre-watch questions
* what are aggregations in spark?
* How do they work internally?
* Why are they used?

## Chunk 1
(only write concepts)

min/max
mean/sum/count
distinct

group by
relationalgroupeddataset
aggregations on group by
wide aggregations
shuffle
usually do aggregations at the end

## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

### 3 main points
1. Aggregations are wide transformations meaning that it involves 1 or more partitions outputing to 1 or more partitions this results in data shuffling and is quite expensive. So aggregations should be used carefully and ideally at the end of the job
2. Spark supports many aggregations like sum/count/countDistinct/mean/stddev/min/max, etc.
3. Spark has two powerful operations **groupBy** which makes a **relationalgroupeddataset** from a dataframe. This is intermediate state that has a dataframe and a groupign strategy so its called a relationalgroupdataset. Once we apply an aggregation then it outputs a dataframe. Additionally it has **agg** functionality which will allow us to do multiple aggregations on the group such as avg another col and summing another.

### Plain english
Aggregations are wide transformations that shuffle data between partitions. They are powerful because they allow us to aggregate data to analyze data in groupings however they are expensive due to shuffling data between nodes.

Many types are supported including sum/count/countDistinct/mean/stddev/min/max

GroupBy allows us to group data frame and apply aggregations to groups. Agg allows us to apply multiple aggregations on a dataframe.

### why it matters 
Aggregations let us analyize groupings of big data.


## Chunk 1 compressed
Concept: Aggregations help us understand groups of rows in big data
Why it matters: can be used to analyze aggregates
Example: Group all ad clicks dataset by ads and count the number of clicks and impressions. Then we can sort to see the best performing ads
One confusion: aggregations are **Expensive** since they require **Shuffling** data 
