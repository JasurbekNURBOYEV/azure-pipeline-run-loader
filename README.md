# azure-pipeline-run-loader
Load &amp; save all your Pipeline runs in Azure DevOps locally

# Configuration
There are 2 things to set-up before using the tool.
1. Personal access token. You get it from [here](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)
2. Organization URL. This is something like this `https://dev.azure.com/YOUR_ORGANIZATION`. 
   This URL is present in browser when you log-in to Azure DevOps. 
These can be either manually configured inside `config.json` file, in project folder, 
or it will be automatically created when you run the tool.

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
