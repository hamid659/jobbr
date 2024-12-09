import logging
import requests
from jobbr.simulator import JobAPISimulator  # Import the simulator

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
    def __init__(self, base_url, api_key, simulate=False):
        """
        Initializes the JobAPIClient.

        :param base_url: The base URL for the API.
        :param api_key: The API key for authorization.
        :param simulate: Flag to toggle between real and simulated API requests.
        """
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.simulate = simulate  # Flag to toggle between real and simulated requests

    # @retry(
    #     stop=stop_after_attempt(3),
    #     wait=wait_exponential(multiplier=1, min=2, max=10),
    #     retry=retry_if_exception_type(requests.exceptions.RequestException)
    # )

    def _make_request(self, method, endpoint, **kwargs):
        """
        Makes the API request. If simulate is True, it uses simulated data.

        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: The API endpoint to hit.
        :param kwargs: Additional arguments for the request (like payload, parameters).
        :return: The response from the API or simulated data.
        """
        if self.simulate:
            # Simulate the response based on the endpoint
            if endpoint == "/jobs":
                return JobAPISimulator.simulate_get_jobs()
            elif endpoint == "/jobs/queue":
                return JobAPISimulator.simulate_get_queued_jobs()
            elif 'queue' in endpoint:
                return JobAPISimulator.simulate_queue_job(kwargs.get('json', {}).get('job_id'))
            elif '/jobs' in endpoint:
                return JobAPISimulator.simulate_create_job(kwargs.get('json', {}))
            else:
                return {"error": "Unknown endpoint"}

        # If simulation is off, make a real request
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Return response body as JSON
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during request to {url}: {e}")
            raise

    def get_jobs(self):
        """
        Fetches all jobs from the API.

        :return: The list of jobs (simulated or real).
        """
        try:
            response = self._make_request("GET", "/jobs")
            logger.info("Fetched jobs successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch jobs: {e}")
            return {"error": str(e)}

    def get_queued_jobs(self):
        """
        Fetches the list of queued jobs.

        :return: The list of queued jobs (simulated or real).
        """
        try:
            response = self._make_request("GET", "/jobs/queue")
            logger.info("Fetched queued jobs successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch queued jobs: {e}")
            return {"error": str(e)}

    def queue_job(self, job_id):
        """
        Queues a specific job by ID.

        :param job_id: The ID of the job to be queued.
        :return: The result of the queue operation (simulated or real).
        """
        try:
            response = self._make_request("POST", f"/jobs/{job_id}/queue", json={"job_id": job_id})
            logger.info(f"Queued job {job_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to queue job {job_id}: {e}")
            return {"error": str(e)}

    def create_job(self, job_data):
        """
        Creates a new job.

        :param job_data: A dictionary containing the job data.
        :return: The result of the job creation (simulated or real).
        """
        try:
            response = self._make_request("POST", "/jobs", json=job_data)
            logger.info(f"Created job successfully: {job_data}")
            return response
        except Exception as e:
            logger.error(f"Failed to create job: {e}")
            return {"error": str(e)}
