import db
from client import Client
import configs


def main():
    config = configs.load_configs()
    if not config:
        config = configs.create_config()

    db_connection = db.get_db_connection()
    try:
        db.create_table(db_connection)
    except:  # noqa
        pass

    client = Client(pat=config.personal_access_token, organization_url=config.organization_url)
    projects = list(client.get_projects())

    for ind, project in enumerate(projects):
        print(f"[{ind}] {project.name}")
    print(f"[{len(projects)}] All")

    project_selection = input("Choose a project number to collect pipeline runs for: ")
    if not project_selection.isnumeric():
        raise ValueError("You should choose number")
    project_selection = int(project_selection)
    if 0 <= project_selection < len(projects):
        selected_projects = [projects[project_selection]]
    elif project_selection == len(projects):
        selected_projects = projects
    else:
        raise ValueError(f"Choice must be between 0 and {len(projects)}")

    for project in selected_projects:
        print(f"Getting pipeline runs for project {project.name}")
        for run in client.get_pipeline_runs(project.name):
            print(f" {run.run_name}")
            db.insert(db_connection, run)
            db_connection.commit()
        print("-" * 50)
    print("Finished")
    db_connection.close()


if __name__ == "__main__":
    main()
