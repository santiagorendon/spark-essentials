import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, DateType
from pyspark.sql import Row


def require_java() -> None:
    java_home = os.environ.get("JAVA_HOME")
    java_on_path = shutil.which("java")

    if java_home and java_on_path:
        return

    raise SystemExit(
        "Java is required to run PySpark.\n"
        "Install JDK 11+ and set JAVA_HOME to your JDK folder, for example:\n"
        "  $env:JAVA_HOME='C:\\Program Files\\Java\\jdk-17'\n"
        "Then add Java to PATH for this shell:\n"
        "  $env:Path = \"$env:JAVA_HOME\\bin;\" + $env:Path\n"
    )


require_java()

# Create Spark session
spark = SparkSession.builder \
    .appName("Data Sources and Formats") \
    .config("spark.master", "local") \
    .getOrCreate()


carSchema = StructType([
    StructField("Name", StringType(), True),
    StructField("Miles_per_Gallon", DoubleType(), True),
    StructField("Cylinders", LongType(), True),
    StructField("Displacement", DoubleType(), True),
    StructField("Horsepower", LongType(), True),
    StructField("Weight_in_lbs", LongType(), True),
    StructField("Acceleration", DoubleType(), True),
    StructField("Year", DateType(), True),
    StructField("Origin", StringType(), True),
])



# read a DF with your schema
# - format
# - schema (optional)
# - zero or more options .option("inferSchema", "true")
# - one of the options is mode - which lets us say how to tread fauly rows, there is drop malformed or permissive which is default
carsDF = spark.read \
    .format("json").schema(carSchema).option("mode", "failFast").load("src/main/resources/data/cars.json")

# pass in several options with a map
carsDFWithOptionMap = spark.read.format("json").options(mode= "failFast", inferSchema= "true").load("src/main/resources/data/cars.json")

# carsDFWithOptionMap.show()


# writing data frames
# format - requires setting a format 
# save mode - requires save mode = overwrite, append, ignore, errorIfExists - what to do if file already exists
# path
# zero or more options
# output:
# _SUCCESS file - marks that spark finished
# several partial files depending on how large the data was
carsDF.write.format("json").mode("overwrite").save("src/main/resources/data/datasources/cars_dupe.json")


# PART 2 - various formats and flags to data sources


# json flags
# date format only works with enforced schema, so need to specify one
# date format - couple with schema; if spark fails parsing it will put null
# compression defaults to uncopressed but can be useful for large files - it supports gzip and others
# do not need to put .format("json") - just change .load to .json
spark.read.option("dateFormat", "YYYY-MM-dd") \
    .option("allowSingleQuotes", "true") \
    .option("compression", "uncompressed") \
    .schema(carSchema) \
    .json("src/main/resources/data/cars.json")


# csv flags
# csv has most than other types since they support so many things that they are more complex
stocksSchema = StructType([
    StructField("symbol", StringType()),
    StructField("date", DateType()),
    StructField("price", DoubleType())
])

# most important csv specific options
# csvs might not have headers so you should tell it so we can ignore first row
# sep - specify the seperator
# nullValue - tell spark which is null value in csv since its not a normal type supported in csv
spark.read \
    .schema(stocksSchema) \
    .option("dateFormat", "MMM dd YYYY") \
    .option("header", "true") \
    .option("sep", ",") \
    .option("nullValue", "") \
    .csv("src/main/resources/data/stocks.csv")

# parquet
# open source compressed binary storage format, optimized for fast reading of columns
# parquet is default storage format of data frames because its very good
# parquet are very predictable so need a lot less options
# parquet is DEFAULT so i can just put save instead of .parquet 
carsDF.write \
    .mode("overwrite") \
    .parquet("src/main/resources/data/datasources/cars.parquet")

# text file
# can even read from text files
# spark.read.text("src/main/resources/data/sampleTextFile.txt").show()

# reading from a remote DB
employeesDF = spark.read \
    .format("jdbc") \
    .option("driver", "org.postgresql.Driver") \
     .option("url", "jdbc:postgresql://postgres:5432/rtjvm") \
    .option("user", "docker") \
    .option("user", "docker") \
    .option("password", "docker") \
    .option("dbtable", "public.employees") \
    .load()


# exercise
# read movies dataframe - DONE
# write it as 
# - tab seperated values file
# - snappy parquet
# - write it in table in postgres db called "public.movies"


# read movies dataframe
moviesDF = spark.read \
    .format("json") \
    .option("inferSchema", "true") \
    .load("src/main/resources/data/movies.json")

moviesDF.show()


# write it as tab seperated csv (TSV)
moviesDF.write \
    .format("csv") \
    .option("sep", "\t") \
    .option("header", "true") \
    .mode("overwrite") \
    .option("nullValue", "") \
    .save("src/main/resources/data/datasources/movies.csv")


# write as parquet - parquet is DEFAULT so format is not needed here
moviesDF.write \
    .format("parquet") \
    .mode("overwrite") \
    .save("src/main/resources/data/datasources/movies.parquet")


# write it to postgres table
moviesDF.write \
    .format("jdbc") \
    .option("driver", "org.postgresql.Driver") \
    .option("url", "jdbc:postgresql://postgres:5432/rtjvm") \
    .option("user", "docker") \
    .option("user", "docker") \
    .option("password", "docker") \
    .option("dbtable", "public.movies") \
    .save()


spark.stop()