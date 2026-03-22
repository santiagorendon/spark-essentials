# Title

## Pre-watch questions

## Chunk 1
(only write concepts)


## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

# 3 main points
1. can also run spark sql programmatically and not just in shell
2. spark.sql command lets you run any commands that we could from shell like creating database, creating table, or even running sql on tables
3. We can create tables:
    3.1 and insert values manually
    3.2. or convert outside databases to tables by transfering them
    3.3. or finally convert any dataframe into a table with createOrReplaceView

# plain english
We can transform existing dataframes, or outsides db tables into spark tables then we can run spark sql on them. Spark sql command lets you run any command that you can do in shell like creating db, creating table, inserting into table, and finally and most importantly running sql

## Chunk 1 compressed
Concept: lets you run sql using spark 
Why it matters: high level access using sql which a lot of ppl are comfortable with 
Example: ad hoc analysis of tables using sql 
One confusion: when running spark sql we read spark tables but they normally return spark dataframes that we can use .show() to see results
