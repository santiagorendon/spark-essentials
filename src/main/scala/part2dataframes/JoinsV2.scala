package part2dataframes

import org.apache.spark.sql.SparkSession
import part2dataframes.Joins.bandsDF
import org.apache.spark.sql.functions.expr

object JoinsV2 extends App {
  val spark = SparkSession.builder()
    .appName("Joins")
    .master("local[*]")
    .getOrCreate()

  val guitarsDF = spark.read
    .option("inferSchema", "true")
    .json("src/main/resources/data/guitars.json")

  val guitaristsDF = spark.read
    .option("inferSchema", "true")
    .json("src/main/resources/data/guitarPlayers.json")

  val bandDF = spark.read
    .option("inferSchema", "true")
    .json("src/main/resources/data/bands.json")

  val guitaristsBandsDF =
    guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "inner")

  // outer joins
  // left outer = everything in the inner join + all the rows in the LEFT table, with nulls where the data is missing
  guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "left_outer")

  // right outer = everything in the inner join + all the rows in the RIGHT table, with nulls where the data is missing
  guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "right_outer")

  // full outer join = everything in RIGHT and LEFT TABLES, with nulls where data is missing
  guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "outer")

  // semi-joins = everything in the left DF for which there is a row in the right DF satisying the condition
  guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "left_semi")

  // anti-join = everything in the left DF for which there is NO row in the right DF satisying the condition
  guitaristsDF.join(bandDF, guitaristsDF.col("band") === bandDF.col("id"), "left_anti").show

  // things to bear in mind
  // if both columns have colliding columns spark will crash when refering to them
  // gu9itaristsBandDF.select("id", "band").show this crashes

  // option 1 - rename the column on which we are joining
  guitaristsDF.join(bandDF.withColumnRenamed("id", "band"), "band")

  // option 2 - drop the dupe column, make sure to pass col of the other dataframe.
  guitaristsBandsDF.drop(bandDF.col("id"))

  // option 3 - rename the offending column and keep the data
  val bandsModDF = bandDF.withColumnRenamed("id", "bandId")
  guitaristsDF.join(bandsModDF, guitaristsDF.col("band") === bandsModDF.col("bandId"), "inner")


  // using complex types to join, use expression to make any join on any condition
  guitaristsDF.join(guitarsDF.withColumnRenamed("id", "guitarId"), expr("array_contains(guitars, guitarId)"))


  spark.stop()
}