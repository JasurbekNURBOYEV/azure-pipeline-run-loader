from typing import Iterable
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import extractors as extract
from models import RunInfo, Project


class Client:
    def __init__(self, pat: str, organization_url: str):
        self.pat = pat
        self.organization_url = organization_url
        self._credentials = BasicAuthentication('', pat)
        self._connection = Connection(base_url=organization_url, creds=self._credentials)
        self._pipelines = None
        self._core = None

    @property
    def pipeline(self):
        if self._pipelines is None:
            self._pipelines = self._connection.clients.get_pipelines_client()
        return self._pipelines

    @property
    def core(self):
        if self._core is None:
            self._core = self._connection.clients.get_core_client()
        return self._core

    def get_projects(self) -> Iterable[Project]:  # noqa
        for project in self.core.get_projects():
            yield project

    def get_pipeline_runs(self, project_name: str) -> Iterable[RunInfo]:
        for pipeline in self.pipeline.list_pipelines(project_name):
            for run in self.pipeline.list_runs(project=project_name, pipeline_id=pipeline.id):
                if run.finished_date and run.created_date:
                    duration = (run.finished_date - run.created_date).seconds
                else:
                    duration = None
                repo_name = extract.repo_name_from_run(run)
                repo_uri = extract.repo_uri_from_run(run)
                folder = extract.folder_name_from_pipeline(pipeline)

                yield RunInfo(
                    project=project_name,
                    pipeline_name=pipeline.name,
                    pipeline_id=pipeline.id,
                    repo_uri=repo_uri,
                    repo_name=repo_name,
                    created_date=run.created_date,
                    finished_date=run.finished_date,
                    duration_seconds=duration,
                    folder=folder,
                    run_id=run.id,
                    run_name=run.name,
                )
