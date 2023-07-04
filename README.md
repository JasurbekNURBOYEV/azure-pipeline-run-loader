# azure-pipeline-run-loader
Load &amp; save all your Pipeline runs in Azure DevOps locally

# Configuration
There are 2 things to prepare before using the tool.
1. Personal access token. You get it from [here](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)
2. Organization URL. This is something like this `https://dev.azure.com/YOUR_ORGANIZATION`. 
   This URL is present in browser when you log in to Azure DevOps. 

If you don't have these values, please obtain them. You'll be asked to enter them when you run the tool.
By default, you don't have to do anything before running the tool. 
Config file will be created automatically once you run the tool.
But if you want to set them manually, create `config.json` file at the root directory of the project,
and copy & paste the content of `config_structure.json` into it, then replace values with your own values.

# Usage

## Create virtual environment and activate it

On macOS and Linux
```shell
python -m venv venv
source venv/bin/activate
```

On Windows
```shell
python -m venv venv
venv\Scripts\activate
```

## Install requirements
```shell
pip install -r requirements.txt
```

## Run
```shell
python src/main.py
```

# Result
You should see `runs.db` file at the root directory of the project.
It contains table called `pipeline_runs`, including all pipeline runs, in a single table.

# Duplication
Tool is not idempotent. When you run the tool multiple times, you may have duplicate values in database. 
So, the best way would be to delete `runs.db` before running the tool each time.
