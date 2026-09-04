# Databricks Sales Capstone Project  

End-to-end ETL pipeline: Bronze → Data Quality → Silver → Gold, orchestrated via Databricks Jobs 
and deployed using Databricks Asset Bundles with GitHub Actions CI/CD.

## Pipeline stages
1. Bronze ingestion from raw CSV in a Unity Catalog Volume
2. Data quality report (flags invalid records)
3. Silver layer (cleaned, typed, valid records only)
4. Gold layer (aggregated sales summary by year/month/state/category)
5. SQL Dashboard on top of the gold table
