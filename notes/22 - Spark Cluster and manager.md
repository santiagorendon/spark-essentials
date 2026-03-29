# Title

## Pre-watch questions
* How does spark manage the cluster?
* What are main components?

## Chunk 1
(only write concepts)


cluster manager
yarn
standalone
mesos
driver
executor
execution modes (cluster, client, local)


## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

### 3 main points
1. Spark has main components of spark cluster manager, spark driver, and spark executors.
2. Cluster has main components cluster driver and cluster workers not to get confused with spark driver and spark executors.
3. Spark cluster manager will manage spark executors using spark driver as an interface. The driver will hold the state and plan of executors. The executors will be doing the actual computations.


### Plain english
spark cluster manager, manages the executors through the spark driver. executor does the actual business logic execution. 

There are 3 main modes - cluster, local, client

local - everything on one machine
client - driver runs on client machine as well as cluster manager
cluster - all nodes run on a cluster executors and cluster manager and driver.

spark-submit is the binary that we run to start a spark job, in it you can pass the code to execute as well as the mode (client, local, cluster) and finally any arguments to pass into the function that will be executed.


## Chunk 1 compressed
Concept: The overarching management of spark execution
Why it matters: Knowing components of spark job can help us understand what happens in the background when we execute spark jobs.
Example: spark cluster asks spark driver what to do spark driver sees that executors finished and need to start new ones to read results of old ones.
One confusion: driver is not 1-1 with cluster manager instead cluster manager uses driver to manage executors.

