# Spark dataframes

## Pre-watch questions
* What are dataframes?
* how do we create a dataframe?
* what can we do with dataframes?
* why do we use dataframes?

## Chunk 1
(only write concepts)

distributed collection of rows
schema
row
dataframe
manual df and schema

## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

### 3 main points
1. Dataframe are used to store distributed collection of rows
2. Schema holds the contract for the dataframe
    2.0 dataframe have custom types that map 1-1 to python such as str -> StringType
    2.1 rows themselves do not have schema
    2.2 better to do manual schemas than infer schema in general
3. You can read dataframes from sources or manually create dataframes usually for testing

### plain english
Dataframes hold distributed rows of data. They can be fream sources such as files or external sources. 
Schemas allow us to understand what kind of data is stored. Rows themselves have no schema. 
You can also create your own dataframe row by row or manually construct your own schema for a dataframe.


## Chunk 1 compressed
Concept: dataframes
Why it matters: high level datastructure that allows us to read data in spark
Example: we created a dataframe that stored information about cars
One confusion: manual schemas are usually better than infered schemas. Additionally rows themselves do not have schemas only dataframes do.
