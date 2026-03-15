import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType
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

cars_json_path = Path(__file__).resolve().parents[3] / "src" / "main" / "resources" / "data" / "cars.json"

# Create Spark session
spark = SparkSession.builder \
    .appName("DataFrames Basics") \
    .config("spark.master", "local") \
    .getOrCreate()

firstDF = spark.read \
    .format("json") \
    .option("inferschema", "true") \
    .load("src/main/resources/data/cars.json")

# showing a df
firstDF.show()
firstDF.printSchema()

for row in firstDF.take(10):
    print(row)

# spark types - one for each python type
longType = LongType
stringType = StringType


# schema - in practice its better to construct your own schema rather than infer
# in practice you might have issuews with infer schema and might want to define your own
# ex: you might end up parcing dates in an incorrect way if its not iso standard and thus they might get handled as strings
carSchema = StructType([
    StructField("Name", StringType(), True),
    StructField("Miles_per_Gallon", DoubleType(), True),
    StructField("Cylinders", LongType(), True),
    StructField("Displacement", DoubleType(), True),
    StructField("Horsepower", LongType(), True),
    StructField("Weight_in_lbs", LongType(), True),
    StructField("Acceleration", DoubleType(), True),
    StructField("Year", StringType(), True),
    StructField("Origin", StringType(), True),
])


carsDFSchema = firstDF.schema
print(carsDFSchema)

# read a DF with your schema
carsDFwithSchema = spark.read \
    .format("json").schema(carsDFSchema).load("src/main/resources/data/cars.json")


# create rows by hand - it accepts almost anything as type in Row constructor
myRow = Row("chevrolet chevelle malibu", 18, 8, 307, 130, 3504, 12.0, "1970-01-01", "USA")


# create DF from tuples
cars = [
    ("chevrolet chevelle malibu", 18.0, 8, 307.0, 130, 3504, 12.0, "1970-01-01", "USA"),
    ("buick skylark 320", 15.0, 8, 350.0, 165, 3693, 11.5, "1970-01-01", "USA"),
    ("plymouth satellite", 18.0, 8, 318.0, 150, 3436, 11.0, "1970-01-01", "USA"),
    ("amc rebel sst", 16.0, 8, 304.0, 150, 3433, 12.0, "1970-01-01", "USA"),
    ("ford torino", 17.0, 8, 302.0, 140, 3449, 10.5, "1970-01-01", "USA"),
    ("ford galaxie 500", 15.0, 8, 429.0, 198, 4341, 10.0, "1970-01-01", "USA"),
    ("chevrolet impala", 14.0, 8, 454.0, 220, 4354, 9.0, "1970-01-01", "USA"),
    ("plymouth fury iii", 14.0, 8, 440.0, 215, 4312, 8.5, "1970-01-01", "USA"),
    ("pontiac catalina", 14.0, 8, 455.0, 225, 4425, 10.0, "1970-01-01", "USA"),
    ("amc ambassador dpl", 15.0, 8, 390.0, 190, 3850, 8.5, "1970-01-01", "USA"),
]

manualCarsDF = spark.createDataFrame(cars) # schema auto-inferred
manualCarsDF.show()

# note DFs have schemas unlike rows
manualCarsDFWithImplicits = spark.createDataFrame(cars, ["Name", "MPG", "Cylinders", "Displacement", "HP", "Weight", "Acceleration", "Year", "CountryOrigin"])


# exercise
# 1) create manual df describing smart phones
# - make
# - model
# - screen dimension
# - camera megapixels

iosDFSchema = StructType([
    StructField("make", StringType(), False),
    StructField("model", StringType(), False),
    StructField("screen width", LongType(), False),
    StructField("screen height", LongType(), False)
])

iOSDf = spark.createDataFrame([
    Row("ios", "16 ultra", 250, 1000),
    Row("android", "11 plus", 250, 1000)
], schema=iosDFSchema)

iOSDf.show()


# 2) read another file from the data folder, i.e movies
# - print the schema
# - count the number of rows

# stop spark session

moviesDF = spark.read.format("json").load("src/main/resources/data/movies.json")

moviesDF.show()
moviesDF.printSchema()
print(moviesDF.count())