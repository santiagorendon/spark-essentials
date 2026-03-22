
# Title

## Pre-watch questions
How does spark sql shell work?
How is it different from normal access on dataframe?

## Chunk 1
(only write concepts)

database
table
view
dataframe vs table


see commands in here: C:\Users\santi\OneDrive\Desktop\Workspace\spark-essentials\src\main\scala\part4sql\SparkShell.scala


**IMPORTANT INSTRUCTIONS TO GO TO SHELL** Commands:
1. docker-compose up --scale spark-worker=3
    1.1 find the log that says Container spark-cluster-spark-master-1 Created to see master container name to use in next command
2. run docker exec -it spark-cluser-spark-master-1 bash 
3. run ./bin/spark-sql inside the host this will start a sql shell
4. Run commands 
 4.1 show databases;
 4.2 create database rtjvm
 4.3 use rtjv;
 4.4 create table persons(id integer, name string);
 4.5 select * from persons;
 4.6 insert into persons values (1, "Marin Odersky"), (2, "Matei Zaharia");
 4.7 other sql commands !
 4.8 create external table - create table flights(origin string, destination string) using csv options(header true, path "home/rtjvm/data/flights");
 4.9 insert into external table - insert into flights values ("Los Angeles", "New York"), ("London", "Prague");
5. in bash can wee where the table is stored in this path /spark/spark-warehouse/rtjvm.db/persons#
6. the table is stored in several partitioned filed
7. describe table - describe extended flights
 7.1. this shows us that the table for flights is external one this was like writing to a dataframe that we did in earlier lessons

MANAGED table type
EXTERNAL table type

## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`


### 3 main points
1. spark sql shell - lets you run sql commands on spark tables, for this lesson we did it in spark shell by sshing into the master node
2. table vs dataframe - table is same as dataframe in way its stored and that its distrubuted however dataframe you query programmatically and spark table you query with sql
3. MANAGED v EXTERNAL - managed table spark manages the data and metadata, this means you do not worry about the data but you can drop it from shell and it will get deleted. External you manage the data spark just handles metadata like the schema, if you drop it in spark shell you still keep the data, downside here is you manage the data.

## Chunk 1 compressed
Concept: Spark sql lets you run distributed table transformations in sql on tables 
Why it matters: if you are familiar with sql its higher level apis to manage distributed data
Example: Running spark sql on user metadata tables to run ad hoc analysis on your customers in distributed manner 
One confusion: tables are actually same as dataframe in the way its stored and handled its just that you use sql instead of map/filter/etc 
