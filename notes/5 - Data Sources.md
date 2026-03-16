
# Title

## Pre-watch questions
* What are data sources?
* What types do we support?
* how do we read from them?
* How does spark handle this in background?

## Chunk 1
(only write concepts)

format
schema
option
load
mode
failfast
permissive
drop malformed


## Chunk 1 converted
- the `3 main points`
- the `plain English explanation`
- `why it matters`
- `one example`

# 3 main points
1. DataFrame can read from data sources which can be internal files or external such as s3
    1.1 formats supported include: csv, json, parquet, and more
2. We can pass in format, schema, options, and path to load the data. Some of the options include mode, path.
3. We can write dataframe output as well this outputs a _success file when its done and several partial files with chunks of the dataframe.

# plain english
Dataframes can read from several sources internally and externally. When reading we can pass in several configurations like datasource path, mode, schema, etc. The mode determines how we treat data that does not confirm to schema default is permissive and sets them to null but other options include fail fass or drop malformed. Finally we can write a dataframe you pass in options like path , format and mode. Mode here means things like overwrite, or append, or ignore, which is characteristics on how to behave if something exists in path. We usually write in parallel so it makes several partitions and a success file to dictate it finished.

Options:
For each file type there are different option configurations
json - can say how to treat date times, pass in compression, can pass in to allow for single quotes
csv - can pass in delimeter, can say if header is first line, can pass in what a null value looks like
parquet - very little options needed since already has a lot of data, this works very well with spark and is DEFAULT format that it writes.

Alot of the same options can be used for reading and for writing they are shared.


# why it matters
Reading and writing to datasources helps us be able to read data transform it and load it later. The basis of ETL.

## Chunk 1 compressed
Concept: Data sources is where spark reads data can be external or internal
Why it matters: Basis of ETL is extracting and loading at the end
Example: Reading from cars dataframe and then saving it in different format in different location.
One confusion: With schema conflicts the mode permissive is default and sets the faulty column to null. dropped malformed drops row entirely. fail fast will stop execution and fail the job when encouterning non confirming data.
