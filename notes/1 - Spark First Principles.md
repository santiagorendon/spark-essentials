
# Unified Computing Engine

## Pre-watch questions
* What is spark used for?
* How does it work?
* Why do people use it?
* What are the best practices?


## Chunk 1
(only write concepts)

unified computing engine
big data
data processing tasks
unified
computing vs data
mapreduce

spark 1 - functional api with data sharing
spark 2 - ad-hoc data exploration
spart 3 - ml

why - popular + maintain

spark reading from 3p

rdds
ll apis
distributed variables

dataframes
datasets
spark sql



## Chunk 1 c9onverted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

3 main points
* What is spark
* why do people use it
* what is architecture

plain english
Distributed processing has gotten more important overtime as data growth and storage has outscaled computing improvements.
People used to use map reduce however had many unneccasry steps that made it bad for ml and large applications
apache spark offers low level apis and high level apis then libraries. the higher the level the less control.
Main low level is rdds and main high level is dataframes.

why it matters
allows efficent big data processing and is popularly supported

one example
Needed to do ad-hoc analysis on large customer datasets to understand the business customers better.

## Chunk 1 compressed
Concept: ...
Why it matters: ...
Example: ...
One confusion: ...


Concept: Spark is used for processing big data through high level and low level apis
Why it matters: big data is too large to compute on one machine efficently
Example: understanding a business customers where the business has multiple millions of them
One confusion: people think spark is related to hadoop of worries about data it does not,
spark lets data be handled by other like hdfs, s3, etc. additonally it is not part of hadoop but integrates well with it.



