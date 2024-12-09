import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("jobbr.log"),  # Logs to a file
        logging.StreamHandler()           # Logs to the console
    ]
)
logger = logging.getLogger(__name__)

class JobAPIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'}

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during request to {url}: {e}")
            raise

    def get_jobs(self):
        try:
            response = self._make_request("GET", "/jobs")
            logger.info("Fetched jobs successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch jobs: {e}")

    def get_queued_jobs(self):
        try:
            response = self._make_request("GET", "/jobs/queue")
            logger.info("Fetched queued jobs successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch queued jobs: {e}")

    def queue_job(self, job_id):
        try:
            response = self._make_request("POST", f"/jobs/{job_id}/queue")
            logger.info(f"Queued job {job_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to queue job {job_id}: {e}")

    def create_job(self, job_data):
        try:
            response = self._make_request("POST", "/jobs", json=job_data)
            logger.info(f"Created job successfully: {job_data}")
            return response
        except Exception as e:
            logger.error(f"Failed to create job: {e}")
