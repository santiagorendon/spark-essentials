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
    .appName("Joins") \
    .config("spark.master", "local") \
    .getOrCreate()
    

guitarsDF = spark.read.json("src/main/resources/data/guitars.json")


guitaristsDF = spark.read.json("src/main/resources/data/guitarPlayers.json")



bandsDF = spark.read.json("src/main/resources/data/bands.json")



# join data to add band metadata for guitarists
# inner join - rows that match the condition are combined others are discarded
joinCondition = guitaristsDF["band"] == bandsDF["id"]
guitaristsBandsDF = guitaristsDF.join(bandsDF, joinCondition, "inner")

# result- missing beatles and eric klapton since they did not have entries
# +----+-------+---+------------+-----------+---+------------+----+
# |band|guitars| id|        name|   hometown| id|        name|year|
# +----+-------+---+------------+-----------+---+------------+----+
# |   1|    [1]|  1| Angus Young|     Sydney|  1|       AC/DC|1973|
# |   0|    [0]|  0|  Jimmy Page|     London|  0|Led Zeppelin|1968|
# |   3|    [3]|  3|Kirk Hammett|Los Angeles|  3|   Metallica|1981|
# +----+-------+---+------------+-----------+---+------------+----+

guitaristsBandsDF.show()


# outer joins
# left outer = everything in the inner join + all the rows in the LEFT table
# left outer = everything in inner join + all the rows in the LEFT table, with nulls where data is missing
guitaristsDF.join(bandsDF, joinCondition, "left_outer").show() 


