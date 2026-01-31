from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CheckGold") \
    .getOrCreate()

df = spark.read.parquet("data/lake/gold/platform_ratings")
df.show()
df.printSchema()
