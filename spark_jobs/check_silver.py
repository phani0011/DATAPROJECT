from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CheckSilver") \
    .getOrCreate()

df = spark.read.parquet("data/lake/silver/movies")
df.show()
df.printSchema()
