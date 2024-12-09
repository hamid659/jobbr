# Solution for jobbr

## What this app does?
Jobbr is a command-line tool to interact with a job management API. It allows users to view, create, and manage jobs and job queues seamlessly.

## Setup

- Clone the repository:
``` 
git clone https://github.com/hamid659/jobbr.git
```

- Navigate to the project directory (the outer jobbr folder, containing setup.py and requirements.txt):
```
cd jobbr
```
Note: There are two jobbr folders in this project:
The outer folder is the project root, containing setup.py and requirements.txt.
The inner folder (jobbr/) is the Python package, containing the tool's code (e.g., cli.py and api_client.py).


- Install the package:
```
pip install .
```



### Dependencies
dependencies are automatically installed when you run:
``` 
pip install .  
```

If you encounter any issues or prefer to install the dependencies separately, you can manually install the required dependencies using:
```
pip install -r requirements.txt
```


## Usage
Once installed, the jobbr CLI becomes available.

Command Overview
```
jobbr --help
```


## Testing
Commands

- View All Jobs
``` jobbr view-jobs ```

- View Queued Jobs
``` jobbr view-queued-jobs ```

- Queue a Job
``` jobbr queue-job <job_id> ```

- Create a Job
``` jobbr create-job --name <job_name> --priority <priority_level> ```

## API simulation
The simulate flag has been added to the view_jobs, view_queued_jobs, queue_job, and create_job commands using @click.option('--simulate', is_flag=True, help="Simulate API requests instead of making real ones.").

- When the --simulate flag is provided in the command, it will set simulate=True in the corresponding command function.
- If the flag is not provided, simulate=False will be the default, and the client will behave as it normally would when making real API requests

``` 
jobbr view-jobs --simulate 
```

## Configuration
The tool uses the following environment variables for API authentication and configuration:

- JOBBR_API_URL	    Base URL for the Jobbr API
- JOBBR_API_KEY	    API key for authenticating requests

#### Set these variables before running the tool:

```
export JOBBR_API_URL="https://api.example.com"
export JOBBR_API_KEY="your_api_key"
```



## Logs 

By default, logs are stored in a file named jobbr.log in the current directory. Logs include timestamps, log levels, and error details for easier debugging and monitoring.

