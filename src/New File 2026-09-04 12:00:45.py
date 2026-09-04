import sys
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.getOrCreate()

source_path = sys.argv[1] if len(sys.argv) > 1 else "/Volumes/workspace/ibm/raw_data/sales_source_1500.csv"

df = (spark.read
      .option("header", True)
      .option("inferSchema", True)
      .csv(source_path))

df_bronze = (df
             .withColumn("ingestion_timestamp", F.current_timestamp())
             .withColumn("source_file", F.input_file_name()))

df_bronze.write.format("delta").mode("overwrite") \
    .saveAsTable("workspace.default.capstone_bronze_sales")

print(f"[BRONZE] Loaded {df_bronze.count()} raw records from {source_path}")