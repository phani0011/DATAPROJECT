from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count
import boto3

spark = SparkSession.builder.appName("LakehouseBatchJob").getOrCreate()

# Download from MinIO
s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
)

s3.download_file("lake", "bronze/events.json", "/tmp/events.json")

# -------- Bronze --------
df = spark.read.json("/tmp/events.json")
df.show()

# -------- Silver --------
silver_df = df.select(
    "genre", "movie", "platform", "rating", "timestamp", "user"
)

silver_df.write.mode("overwrite").parquet("/tmp/silver")

# -------- Gold (Business Layer) --------
gold_df = silver_df.groupBy("platform", "movie") \
    .agg(
        avg("rating").alias("avg_rating"),
        count("rating").alias("total_reviews")
    ) \
    .orderBy("platform", "avg_rating", ascending=False)

gold_df.show()

gold_df.write.mode("overwrite").parquet("/tmp/gold")

spark.stop()












