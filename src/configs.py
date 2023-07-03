import json
import os
from pathlib import Path
from typing import Optional
from models import Config


def get_file_path(file_name: str) -> str:
    current_path = Path(os.getcwd())
    file_path = os.path.join(current_path, file_name)
    print(file_path)
    return file_path


def load_configs(file_name: str = "config.json") -> Optional[Config]:
    file_path = get_file_path(file_name)
    print(file_path)
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as f:
        data = json.loads(f.read())
    return Config(**data)


def create_config():
    inputs = {"Enter personal access token": None, "Org URL": None}
    items = iter(inputs.items())
    head, val = next(items)
    finished = False
    while not finished:
        if val is not None:
            val = input(f"{head} ({val}): ") or val
        else:
            val = input(f"{head}: ") or val
        if not val:
            print("Value can not be empty, enter again")
            continue
        inputs[head] = val
        try:
            head, val = next(items)
        except StopIteration:
            break

    pat, url = inputs.values()

    config = Config(personal_access_token=pat, organization_url=url)
    file_path = get_file_path("../config.json")
    with open(file_path, "w") as f:
        f.write(
            json.dumps(
                {
                    "personal_access_token": config.personal_access_token,
                    "organization_url": config.organization_url
                }
            )
        )

    return config
