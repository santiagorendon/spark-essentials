import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, DateType
from pyspark.sql import Row
from pyspark.sql.functions import expr
from pyspark.sql.functions import col

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
    .appName("DF Columns and Expressions") \
    .config("spark.master", "local") \
    .getOrCreate()

carsDF = spark.read \
    .format("json") \
    .option("inferSchema", "true") \
    .json("src/main/resources/data/cars.json")


carsDF.show()

# columns
# allow us to obtain new dataframes out of others by processing the data
# result of the call is a Column object to be used in select 
# it does NOT HAVE ANY DATA INSIDE BY DEFAULT
firstColumn = carsDF["Name"]

# selecting (projection - projecting the dataframe into a new one with fewer cols)
# this creates a new dataframe with only one column of Name
# this is a NARROW TRANSFORMATION meaning data stays in same partition, input - output partition 1-1
carNamesDF = carsDF.select(firstColumn)

# various select methods
carsDF.select(carsDF["Name"], carsDF["Acceleration"], expr("Origin"), col("Name"))

# can also just pass in names
carsDF.select("Name")

# EXPRESSIONS
# select is an example of expressions but there are many more
# an expression allows you to process DF in whichever way you want

simpleExpression = col("Weight_in_lbs")
weightInKgExpression = (col("Weight_in_lbs") / 2.2).alias("Weight_in_kg")

carsDF.select(col("Name"), col("Weight_in_lbs"), weightInKgExpression, expr("Weight_in_lbs / 2.2")).show()

# select expression
carsWithSelectExprWeightsDF = carsDF.selectExpr("Name", "Weight_in_lbs", "Weight_in_lbs / 2.2")

# df processing - adding a new column
carsWithKGs3DF = carsDF.withColumn("Weight_in_kgs_3", col("Weight_in_lbs") / 2.2)

# renaming a columns
carsWithColRenamed = carsDF.withColumnRenamed("Weight_in_lbs", "Weight in pounds")

# careful with column names
carsWithColRenamed.selectExpr("`Weight in pounds`")

# remove a column
carsWithSelectExprWeightsDF.drop("Cylinders", "Displacements")

# filtering both the following do the same
carsDF.filter(col("Origin") != "USA")
carsDF.where(col("Origin") != "USA")
carsDF.filter("Origin = 'USA'")

# chain filters
carsDF.filter(col("Origin") == "USA").filter(col("Horsepower") > 150)
carsDF.filter((col("Origin") == "USA") & (col("Horsepower") > 150))
carsDF.filter("Origin = 'USA' and Horsepower > 150")

# unioning = adding more rows
moreCarsDF = spark.read.option("inferSchema", "true").json("src/main/resources/data/more_cars.json")

allCarsDF = carsDF.union(moreCarsDF) # works if DFs have the same schema

# distinct values

allCountries = carsDF.select("Origin").distinct()


allCountries.show()


# Exercises
# 1. read the movies df
# 2. select 2 columns of your choice
# 3. create new dataframe by summing gross profits - US_Gross, Worldwide_Gross, US_DVD_Sales as total profit
# 4. Filter for all COMEDY comedies from Major_Genre with IMDB_RATING above 7
# 
# for each exercise try to use different ways of doing things, do not use same, be creative and expressive

moviesDF = spark.read.format("json").load("src/main/resources/data/movies.json")


# select two columns of my choice
subsetMoviesDF = moviesDF.select(moviesDF["Title"], "Director")

subsetMoviesDF.show()

# new data frame with gross profits
totalProfit = moviesDF.withColumn("Total Profit", expr("US_Gross + Worldwide_Gross + US_DVD_Sales"))

totalProfit.select("Total Profit").show()

# select all COMEDY movies with rating above 6
moviesDF.filter("Major_Genre = 'Comedy' and IMDB_Rating > 7").select("Title", "Major_Genre", "IMDB_Rating").show()

spark.stop()
