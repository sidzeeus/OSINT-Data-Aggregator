from src.core.fetcher import fetch_external_data
from src.core.processor import transform_github_events
from src.core.storage import save_to_data_lake
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Configured for GitHub's public events API for demonstration
TARGET_API = "https://api.github.com/events"

def run_job(event, context):
    """
    Lambda Handler triggered by AWS EventBridge (Cron).
    Orchestrates the Fetch -> Transform -> Load (ETL) process.
    """
    logger.info("Starting OSINT Aggregation Job")
    
    try:
        # 1. Fetch
        raw_data = fetch_external_data(TARGET_API)
        
        # 2. Transform
        clean_data = transform_github_events(raw_data)
        
        # 3. Load
        save_to_data_lake(clean_data, source_name="github_public")
        
        return {"status": "SUCCESS", "processed_events": clean_data["total_push_events"]}
        
    except Exception as e:
        logger.error(f"Job failed: {str(e)}")
        # In production, this would trigger an SNS alert via CloudWatch metrics
        raise e
