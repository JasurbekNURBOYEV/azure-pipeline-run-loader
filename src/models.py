from dataclasses import dataclass
from datetime import datetime


@dataclass()
class RunInfo:
    project: str
    pipeline_name: str
    pipeline_id: int
    repo_uri: str
    repo_name: str
    created_date: datetime
    finished_date: datetime
    duration_seconds: int
    folder: str
    run_id: int
    run_name: str


@dataclass()
class Config:
    personal_access_token: str
    organization_url: str


@dataclass()
class Project:
    name: str
    url: str
    description: str
