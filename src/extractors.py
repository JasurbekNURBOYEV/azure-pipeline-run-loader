from typing import Optional


def repo_uri_from_run(run) -> Optional[str]:
    key = "system.pullRequest.sourceRepositoryUri"
    if run.variables:
        return run.variables[key].value if key in run.variables else None
    return None


def repo_name_from_run(run) -> Optional[str]:
    uri = repo_uri_from_run(run)
    if uri:
        return uri.split("/")[-1]
    return None


def folder_name_from_pipeline(pipeline) -> str:
    folder = pipeline.folder
    return folder.replace("\\", "")
