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

## Shortcut (for Linux/MacOS users)
Here is a shortcut to use the whole thing. We have 2 scripts: `setup.sh` and `run.sh`.
You need to give the scripts necessary permissions first:
```shell
chmod +xwr setup.sh
chmod +xwr run.sh
```
Then run them
```shell 
./setup.sh
```
It will create Python virtual environment and install dependencies.
```shell
./run.sh
```
This will run the main script. Actually, there are 2 ways to use it:
   1. just run it without any arguments: `./run.sh`. It will get credentials (token and organization url from `config.json`)
   2. run it with 2 arguments: token and organization url. Sample: `./run.sh <token> <organization-url>`

## If you can not use the shortcut scripts
**I explain how to do these things all manually. You can skip the steps below if ou can use the shortcut.** 

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
