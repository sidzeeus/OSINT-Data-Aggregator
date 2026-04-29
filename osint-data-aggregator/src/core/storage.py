import boto3
import json
from datetime import datetime
from src.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)
s3_client = boto3.client('s3')

def save_to_data_lake(payload: dict, source_name: str):
    """Saves data to S3 using hive-style partitioning for efficient querying."""
    now = datetime.utcnow()
    # Partitioning format: source/year=YYYY/month=MM/day=DD/timestamp.json
    key = f"raw/{source_name}/year={now.year}/month={now.strftime('%m')}/day={now.strftime('%d')}/{now.timestamp()}.json"
    
    try:
        s3_client.put_object(
            Bucket=settings.DATALAKE_BUCKET,
            Key=key,
            Body=json.dumps(payload),
            ContentType='application/json'
        )
        logger.info(f"Successfully archived data to S3 key: {key}")
    except Exception as e:
        logger.error(f"Failed to write to S3 Data Lake: {str(e)}")
        raise
