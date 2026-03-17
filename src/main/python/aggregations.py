import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, DateType
from pyspark.sql import Row
from pyspark.sql.functions import expr
from pyspark.sql.functions import col, count, count_distinct, approx_count_distinct, avg, stddev, mean, min, sum

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
    .appName("Aggregations and Grouping") \
    .config("spark.master", "local") \
    .getOrCreate()


moviesDF = spark.read.json("src/main/resources/data/movies.json")


# counting
genresCountDF = moviesDF.select(count(col("Major_Genre"))) # all values except null
genresCountDF.show()

# counting v2 - does same thing
moviesDF.selectExpr("count(Major_Genre)")

# count all rows in data frame and INCLUDE nulls 
moviesDF.select(count("*"))


# count distinct
moviesDF.select(count_distinct(col("Major_Genre"))).show()


# approximate count - used for large datasets
# does not do full scan so it is approximation
moviesDF.select(approx_count_distinct(col("Major_Genre"))).show()


# min and max
minRatingDF = moviesDF.select(min(col("IMDB_Rating")))
moviesDF.selectExpr("min(IMDB_Rating)")


# sum
moviesDF.select(sum("US_Gross"))
moviesDF.selectExpr("sum(US_Gross)")


# avg
moviesDF.select(avg(col("Rotten_Tomatoes_Rating")))
moviesDF.selectExpr("avg(Rotten_Tomatoes_Rating)")


# data science - mean is same as avg operation
moviesDF.select(mean(col("Rotten_Tomatoes_Rating"))).show()
moviesDF.select(stddev(col("Rotten_Tomatoes_Rating"))).show()


# Grouping - group by INCLUDES null
countByGenre = moviesDF.groupBy(col("Major_Genre")).count() # select count(*) group by Major Genre

# average rating by genre
avgRatingByGenreDF = (
    moviesDF
    .groupBy(col("Major_Genre"))
    .avg("IMDB_Rating")
)

# alternative grouping
# aggregate lets you compute multiple aggregations in same dataframe
aggregationsByGenreDF = (
    moviesDF
    .groupBy(col("Major_Genre"))
    .agg(
        count("*").alias("N_movies"),
        avg("IMDB_Rating").alias("Avg_Rating")
    ).orderBy("Avg_Rating")
)
aggregationsByGenreDF.show()


# Exercices
# 1. sum up ALL profits of ALL movies in DF
# 2. count how many distinct directors we have
# 3. show the meand and standard deviation of US gross revenue for movies
# 4. Compute the average IMDB rating and the average US gross revenue PER DIRECTOR, try to see which are best directors with sorting


# Schema

#  |-- Creative_Type: string (nullable = true)
# |-- Director: string (nullable = true)
# |-- Distributor: string (nullable = true)
# |-- IMDB_Rating: double (nullable = true)
# |-- IMDB_Votes: long (nullable = true)
# |-- MPAA_Rating: string (nullable = true)
#  |-- Major_Genre: string (nullable = true)
#  |-- Production_Budget: long (nullable = true)
#  |-- Release_Date: string (nullable = true)
#  |-- Rotten_Tomatoes_Rating: long (nullable = true)
#  |-- Running_Time_min: long (nullable = true)
#  |-- Source: string (nullable = true)
#  |-- Title: string (nullable = true)
#  |-- US_DVD_Sales: long (nullable = true)
#  |-- US_Gross: long (nullable = true)
#  |-- Worldwide_Gross: long (nullable = true)

# 1. sum up ALL profits of ALL movies in DF
moviesDF.select(sum(expr('US_Gross + Worldwide_Gross + US_DVD_Sales'))).show()



# 2. count how many distinct directors we have
print(moviesDF.select(col("Director")).distinct().count())

# or - does not get null 
moviesDF.select(count_distinct(col("Director"))).show()


# 3. show the mean and standard deviation of US gross revenue for movies
grossRevenue = (
    moviesDF.select(
        mean(col("US_Gross")).alias("mean gross"),
        stddev(col("US_Gross")).alias("stddev gross")
    )
)

grossRevenue.show()



# 4. Compute the average IMDB rating and the average US gross revenue PER DIRECTOR, try to see which are best directors with sorting
directorDF = (
   moviesDF.groupBy(col("Director")) 
   .agg(
       avg(col("IMDB_Rating")).alias("Average IMDB Rating"),
       avg(col("US_Gross")).alias("Average US Gross")
   )
) 

directorDF.show()


top10DirectorsByRating = directorDF.orderBy("Average IMDB Rating", ascending=False)

top10DirectorsByRating.show(10)



top10DirectorsByUSGross = directorDF.orderBy("Average US Gross", ascending=False)

top10DirectorsByUSGross.show(10)