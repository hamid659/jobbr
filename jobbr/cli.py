import click
import os
from jobbr.api_client import JobAPIClient


# Read the base URL and API key from environment variables
BASE_URL = os.getenv("JOBBR_API_BASE_URL")  
API_KEY = os.getenv("JOBBR_API_KEY") 

# Validate that the API key is set
if not API_KEY:
    raise ValueError("API key is not set. Please set the JOBBR_API_KEY environment variable.")

# Initialize the API client with the values from environment variables
client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY)

@click.group()
def cli():
    """Jobbr CLI - Manage Jobs and Queues"""
    pass

@cli.command()
def view_jobs():
    """View all jobs"""
    response = client.get_jobs()
    if response.ok:
        jobs = response.json()
        click.echo(f"Jobs: {jobs}")
    else:
        click.echo(f"Failed to fetch jobs: {response.status_code}")

@cli.command()
def view_queued_jobs():
    """View queued jobs"""
    response = client.get_queued_jobs()
    if response.ok:
        jobs = response.json()
        click.echo(f"Queued Jobs: {jobs}")
    else:
        click.echo(f"Failed to fetch queued jobs: {response.status_code}")

@cli.command()
@click.argument('job_id')
def queue_job(job_id):
    """Queue a job by ID"""
    response = client.queue_job(job_id)
    if response.ok:
        click.echo(f"Job {job_id} queued successfully.")
    else:
        click.echo(f"Failed to queue job {job_id}: {response.status_code}")

@cli.command()
@click.option('--name', prompt='Job Name', help='Name of the job')
@click.option('--type', prompt='Job Type', help='Type of the job')
def create_job(name, type):
    """Create a new job"""
    job_data = {"name": name, "type": type}
    response = client.create_job(job_data)
    if response.ok:
        click.echo(f"Job created successfully: {response.json()}")
    else:
        click.echo(f"Failed to create job: {response.status_code}")

if __name__ == '__main__':
    cli()
