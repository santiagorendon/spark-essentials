
# Title

## Pre-watch questions
* How do dataframes parallelize the processing of data?
* where are rows stored in dataframes?
* How do they infer schemas?
* How do they work?

## Chunk 1
(only write concepts)

distributed
spreadsheet
schema
arbitray row count
partitioning
parallelism vs number of nodes
immutable
transformations
* narrow
* wide
* shuffle
lazy evaluation
planning
graph
compile
logical plan
physical plan
optimizations
actions



## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

# three main points
* dataframe is distributed across nodes each of them get the schema and a subset of the rows
* dataframes are executed in parallel and the parallelism has to do with count of nodes and parallelism set
* dataframes are immutable to create a new one you apply transformations, however these transformations are only executed when actions get performed.
* at compile time spark creates a dag plan to plan out the order of operations and the nodes that will handle them.

# plain english
Dataframes help distribute computations across nodes in a cluster. Each node will get a series of row as well as the schema for the dataframe. Nodes can execute these instructions in parallel however each parallelism depends on partitioning and parallelism plan so we do not always use max nodes provided to us. 
At compile time we know the schema of data frame and all the planned transformations. Dataframes are immutable so we create new dataframes when they are transformed. 

There are two kinds of transformations:
* narrow - one partition to one partion (map)
* wide - one or more partitions to many more partitions (sort)

wide transformations usually add *shuffling* which i bad for performance since it moves data across nodes over the network.

Action vs transformation
* transform - describes how to transform the data. Spark does *lazy evaluation* so it does not execute until action takes place.
* action usually reads the data in some way and thus forces the spark code to execute

Compile
* Spark knows the schema
* Spark makes a plan to transform data in for of a graph
* Logical plan - series of steps
* Physical plan - which nodes should execute the steps


## Chunk 1 compressed
Concept: DataFrames parallelize data computations across nodes in a cluster.
Why it matters: This helps us efficently read large data in parallel.
Example: You want to transform customers to split full name into first name and second name. Then you want to sort by last name then you want to output the result. The map transformation creates a new dataframe and is considered a narrow transformation. The sort transformation creates a new dataframe and is considered a wide transformation and results in a shuffle. Spark will know at compile time the order of logic and which nodes will do what. Then at run time we will only evaluate and run the compute on the line where we output the result. (only evaulate when necessary)
One confusion: Having many nodes available does not by itself guarantee high parallelism. Actual parallelism depends mostly on how many tasks Spark can create, which is driven by partitioning and by the execution plan of the transformations. Spark’s core abstraction is a partitioned collection operated on in parallel, so partitions are the main unit that determines how much work can run concurrently.
