from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MovieAnalytics") \
    .getOrCreate()

# Read bronze data
df = spark.read.json("data/lake/bronze/events.json")

print("=== BRONZE DATA ===")
df.show()

# Silver layer: clean data
silver = df.select("movie", "genre", "platform", "rating")

silver.write.mode("overwrite").parquet("data/lake/silver/movies")

# Gold layer: analytics
gold = silver.groupBy("platform").avg("rating")

gold.write.mode("overwrite").parquet("data/lake/gold/platform_ratings")

print("=== PIPELINE COMPLETED ===")

