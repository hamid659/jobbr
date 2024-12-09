import click
import os
from jobbr.api_client import JobAPIClient


# Read the base URL and API key from environment variables
BASE_URL = os.getenv("JOBBR_API_BASE_URL")  
API_KEY = os.getenv("JOBBR_API_KEY") 

# Define a global simulate flag that can be toggled in CLI commands
simulate_flag = False

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
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def view_jobs(simulate):
    """View all jobs"""
    # Use the simulate flag to toggle simulation mode
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.get_jobs()
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Jobs: {response}")

@cli.command()
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def view_queued_jobs(simulate):
    """View queued jobs"""
    # Use the simulate flag to toggle simulation mode
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.get_queued_jobs()
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Queued Jobs: {response}")

@cli.command()
@click.argument('job_id')
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def queue_job(job_id, simulate):
    """Queue a job by ID"""
    # Use the simulate flag to toggle simulation mode
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.queue_job(job_id)
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Job {job_id} queued successfully.")

@cli.command()
@click.option('--name', prompt='Job Name', help='Name of the job')
@click.option('--type', prompt='Job Type', help='Type of the job')
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def create_job(name, type, simulate):
    """Create a new job"""
    job_data = {"name": name, "type": type}
    # Use the simulate flag to toggle simulation mode
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.create_job(job_data)
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Job created successfully: {response}")

@cli.command()
@click.argument('job_id')
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def delete_job(job_id, simulate):
    """Delete a job by ID"""
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.delete_job(job_id)
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Job {job_id} deleted successfully.")

@cli.command()
@click.argument('job_id')
@click.option('--name', prompt='New Job Name', help='Updated name of the job')
@click.option('--type', prompt='New Job Type', help='Updated type of the job')
@click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.")
def update_job(job_id, name, type, simulate):
    """Update an existing job"""
    job_data = {"id": job_id, "name": name, "type": type}
    client = JobAPIClient(base_url=BASE_URL, api_key=API_KEY, simulate=simulate)
    response = client.update_job(job_id, job_data)
    if isinstance(response, dict) and "error" in response:
        click.echo(f"Error: {response['error']}")
    else:
        click.echo(f"Job {job_id} updated successfully: {response}")


if __name__ == '__main__':
    cli()
