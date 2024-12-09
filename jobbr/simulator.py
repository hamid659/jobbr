import json

class JobAPISimulator:
    @staticmethod
    def simulate_get_jobs():
        # Simulated response for the /jobs endpoint
        jobs_data = [
            {"id": 1, "name": "Job 1", "status": "completed"},
            {"id": 2, "name": "Job 2", "status": "queued"},
        ]
        return json.dumps(jobs_data)  # Simulating a JSON response

    @staticmethod
    def simulate_get_queued_jobs():
        # Simulated response for the /jobs/queue endpoint
        queued_jobs_data = [
            {"id": 2, "name": "Job 2", "status": "queued"}
        ]
        return json.dumps(queued_jobs_data)

    @staticmethod
    def simulate_queue_job(job_id):
        # Simulated response for queuing a job
        return json.dumps({"message": f"Job {job_id} queued successfully."})

    @staticmethod
    def simulate_create_job(job_data):
        # Simulated response for creating a new job
        return json.dumps({"id": 3, "name": job_data["name"], "status": "queued"})
