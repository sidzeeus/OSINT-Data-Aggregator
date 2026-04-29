# OSINT Data Aggregator
An automated, serverless ETL (Extract, Transform, Load) pipeline that fetches external public data, normalizes it, and archives it into an S3 Data Lake.

## Architecture
AWS EventBridge triggers an AWS Lambda function on an hourly schedule. The Lambda function acts as a robust ETL worker. It safely requests external APIs (handling timeouts), maps the messy JSON into a normalized schema, and saves the output to S3 using Hive-style date partitioning (e.g., `/year=2024/month=03/day=15/`).

## Key Features
* **Resiliency:** Implements strict timeouts and request error handling to prevent Lambda function hangs.
* **Data Lake Ready:** S3 objects are formatted in a way that allows AWS Athena to query the data efficiently via partitions.

## Setup Instructions
1. Create an S3 Bucket for the Data Lake.
2. Provide Lambda with `s3:PutObject` IAM permissions.
3. Add a Lambda trigger using Amazon EventBridge with a cron expression (e.g., `cron(0 * * * ? *)` for hourly).
4. Set environment variable `DATALAKE_BUCKET`.
