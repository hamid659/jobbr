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
        if not job_id:
            return {"error": "Job ID is required to queue a job."}
        return json.dumps({"message": f"Job {job_id} queued successfully."})

    @staticmethod
    def simulate_create_job(job_data):
        # Simulated response for creating a new job
        if not job_data or not job_data.get("name"):
            return {"error": "Job name is required to create a job."}
        return json.dumps({"id": 3, "name": job_data["name"], "status": "queued"})

    @staticmethod
    def simulate_delete_job(job_id):
        """
        Simulate a response for deleting a job.
        """
        if not job_id:
            return {"error": "Job ID is required to delete a job."}
        return {"message": f"Job {job_id} deleted successfully."}

    @staticmethod
    def simulate_update_job(job_data):
        """
        Simulate a response for updating a job.
        """
        if not job_data or not job_data.get("id"):
            return {"error": "Job ID and update data are required."}
        return {
            "id": job_data.get("id"),
            "name": job_data.get("name", "Updated Job"),
            "type": job_data.get("type", "default"),
            "status": "updated"
        }