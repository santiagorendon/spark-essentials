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

# Reading a DF
firstDF = spark.read \
    .format("json") \
    .option("inferSchema", "true") \
    .load(str(cars_json_path))

# Showing a DF
firstDF.show()
firstDF.printSchema()

# Get rows
rows = firstDF.take(10)
for row in rows:
    print(row)

# Spark types
longType = LongType()
stringType = StringType()
# ...

# Create schema
carsSchema = StructType([
    StructField("Name", StringType(), True),
    StructField("Miles_per_Gallon", DoubleType()),
    StructField("Cylinders", LongType()),
    StructField("Displacement", DoubleType()),
    StructField("Horsepower", LongType()),
    StructField("Weight_in_lbs", LongType()),
    StructField("Acceleration", DoubleType()),
    StructField("Year", StringType()),
    StructField("Origin", StringType())
])

# Obtain a schema
carsDFSchema = firstDF.schema

# Read a DF with your schema
carsDFWithSchema = spark.read \
    .format("json") \
    .schema(carsDFSchema) \
    .load(str(cars_json_path))

# Create rows by hand
myRow = Row("chevrolet chevelle malibu", 18, 8, 307, 130, 3504, 12.0, "1970-01-01", "USA")

# Create DF from tuples
cars = [
    ("chevrolet chevelle malibu", 18, 8, 307, 130, 3504, 12.0, "1970-01-01", "USA"),
    ("buick skylark 320", 15, 8, 350, 165, 3693, 11.5, "1970-01-01", "USA"),
    ("plymouth satellite", 18, 8, 318, 150, 3436, 11.0, "1970-01-01", "USA"),
    ("amc rebel sst", 16, 8, 304, 150, 3433, 12.0, "1970-01-01", "USA"),
    ("ford torino", 17, 8, 302, 140, 3449, 10.5, "1970-01-01", "USA"),
    ("ford galaxie 500", 15, 8, 429, 198, 4341, 10.0, "1970-01-01", "USA"),
    ("chevrolet impala", 14, 8, 454, 220, 4354, 9.0, "1970-01-01", "USA"),
    ("plymouth fury iii", 14, 8, 440, 215, 4312, 8.5, "1970-01-01", "USA"),
    ("pontiac catalina", 14, 8, 455, 225, 4425, 10.0, "1970-01-01", "USA"),
    ("amc ambassador dpl", 15, 8, 390, 190, 3850, 8.5, "1970-01-01", "USA")
]
manualCarsDF = spark.createDataFrame(cars)  # schema auto-inferred

# Note: DFs have schemas, rows do not

# Create DFs with implicits (in Python, we can use toDF)
manualCarsDFWithImplicits = spark.createDataFrame(cars, ["Name", "MPG", "Cylinders", "Displacement", "HP", "Weight", "Acceleration", "Year", "CountryOrigin"])

# Stop Spark session
spark.stop()
