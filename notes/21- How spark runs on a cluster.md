# Title

## Pre-watch questions
* how does spark distribute data across nodes?
* How do we go from code to query plan to execution?

## Chunk 1
(only write concepts)

dags
stages
tasks
jobs
shuffles
if we do rdd1 = sc.parallelize([0] * 1000000) and we then do repartition(23) we get two stages one stage with default partitions that constructs the rdd and then another stage is created due to the repartition.
.explain
.explain(True) - full plan with physical optimized and logical plans

Commands

1. docker-compose up --scale spark-worker=3
    1.1 find the log that says Container spark-cluster-spark-master-1 Created to see master container name to use in next command
2. run docker exec -it spark-cluster-spark-master-1 bash 
3. run ./bin/pyspark inside the host this will start a spark shell
    3.1 run ./bind/spark-shell for scala version
4. access localhost:4040 to see spark UI, see it in vscode using browser show command and entering the url
5. In this shell you can run spark 


Commands
```
>>> rdd1 = sc.parallelize([x for x in range(1000000)])
>>> rdd1.count()
1000000
>>> rdd1.getNumPartitions()
32
>>> rdd2 = rdd1.map(lambda x: x * 2)
>>> rdd2.count()
1000000
>>> rdd1.repartition(23).count()
1000000
>>> rdd1.toDF().show()
>>> df1 = spark.range(1, 1000000, 2)
>>> df1.explain()
== Physical Plan ==
*(1) Range (1, 1000000, step=2, splits=32)
```

### Reading plans
```
>>> df2 = spark.range(1, 10000000, 5)
>>> df3 = df1.repartition(7)
>>> df3.explain()
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- Exchange RoundRobinPartitioning(7), REPARTITION_BY_NUM, [plan_id=58]
   +- Range (1, 1000000, step=2, splits=32)


>>> df4 = df2.repartition(9)
>>> df4.explain()
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- Exchange RoundRobinPartitioning(9), REPARTITION_BY_NUM, [plan_id=66]
   +- Range (1, 10000000, step=5, splits=32)


>>> df5 = df3.selectExpr("id * 5 as id")
>>> df5.explain()
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- Project [(id#21L * 5) AS id#34L]
   +- Exchange RoundRobinPartitioning(7), REPARTITION_BY_NUM, [plan_id=77]
      +- Range (1, 1000000, step=2, splits=32)


>>> joined = df5.join(df4, "id")
>>> joined.explain()
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- Project [id#34L]
   +- BroadcastHashJoin [id#34L], [id#28L], Inner, BuildLeft, false
      :- BroadcastExchange HashedRelationBroadcastMode(List(input[0, bigint, false]),false), [plan_id=108]
      :  +- Project [(id#21L * 5) AS id#34L]
      :     +- Exchange RoundRobinPartitioning(7), REPARTITION_BY_NUM, [plan_id=101]
      :        +- Range (1, 1000000, step=2, splits=32)
      +- Exchange RoundRobinPartitioning(9), REPARTITION_BY_NUM, [plan_id=104]
         +- Range (1, 10000000, step=5, splits=32)


>>> sum = joined.selectExpr("sum(id)")
>>> sum.explain()
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- HashAggregate(keys=[], functions=[sum(id#34L)])
   +- Exchange SinglePartition, ENSURE_REQUIREMENTS, [plan_id=151]
      +- HashAggregate(keys=[], functions=[partial_sum(id#34L)])
         +- Project [id#34L]
            +- BroadcastHashJoin [id#34L], [id#28L], Inner, BuildLeft, false
               :- BroadcastExchange HashedRelationBroadcastMode(List(input[0, bigint, false]),false), [plan_id=146]
               :  +- Project [(id#21L * 5) AS id#34L]
               :     +- Exchange RoundRobinPartitioning(7), REPARTITION_BY_NUM, [plan_id=137]
               :        +- Range (1, 1000000, step=2, splits=32)
               +- Exchange RoundRobinPartitioning(9), REPARTITION_BY_NUM, [plan_id=140]
                  +- Range (1, 10000000, step=5, splits=32)
```

## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`


### 3 main points
1. spark shell lets you execute commands on master node and these will kick of spark jobs which you can monitor in spark ui.
2. spark jobs are broken down into stages and tasks. stages are split between shuffles, usually shuffles incur a new stage. tasks are split by partitions so each task will execute on one partition of data. Hierarchy is jobs - stages - tasks.
3. you can use .explain() and dag ui to try to understand what spark actually does with your data. 


### Plain english
spark runs your code in a cluster. Each job will have several stages and each stage can have several tasks. Spark optimizer will create a plan based on your spark code and then execute it in a distributed manner. Stage will hold all data then shuffles kick off new stages, tasks will hold partitions of data and execute transforms on them.

## Chunk 1 compressed
Concept: Understanding spark ui is essential to becoming proficent in spark.
Why it matters: Imagine you have job that is slow you look at spark ui and can see the plan and see bottlenecks
Example: Some tasks slower than others you can notice partition skew, spark ui is very useful.
One confusion: spark will make plans based on you code however they also have optimizer so not everything will actually run. Another confusion is that a spark job will actually recompute rdds already computed in other jobs at times unless we cache those rdds 
