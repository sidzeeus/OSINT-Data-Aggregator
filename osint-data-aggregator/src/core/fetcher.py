import requests
from requests.exceptions import RequestException, Timeout
from src.utils.logger import get_logger

logger = get_logger(__name__)

def fetch_external_data(api_url: str, headers: dict = None) -> list:
    """Fetches data from an external API with robust error handling and timeouts."""
    try:
        logger.info(f"Initiating request to {api_url}")
        # Always use timeouts in Serverless to prevent infinite billing!
        response = requests.get(api_url, headers=headers, timeout=5.0)
        
        # Raise HTTP errors (4xx, 5xx)
        response.raise_for_status()
        
        return response.json()
        
    except Timeout:
        logger.error(f"Request to {api_url} timed out.")
        raise Exception("External API timeout")
    except RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        raise Exception("External API communication failure")
