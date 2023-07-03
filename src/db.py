import sqlite3
from models import RunInfo

DB_NAME = "runs.db"


def get_db_connection(db_name: str = DB_NAME):
    con = sqlite3.connect(db_name, isolation_level=None)
    return con


def create_table(con):
    create_query = """
    CREATE TABLE pipeline_runs ( 
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        project TEXT, 
        pipeline_name TEXT, 
        pipeline_id INT, 
        repo_uri TEXT,
        repo_name TEXT,
        created_date DATETIME,
        finished_date DATETIME,
        duration_seconds INT,
        folder TEXT,
        run_id INT,
        run_name TEXT
    )
    """
    con.execute(create_query)


def insert(con, run_info: RunInfo):
    query = """
    INSERT INTO pipeline_runs (
        project, 
        pipeline_name, 
        pipeline_id, 
        repo_uri,
        repo_name,
        created_date,
        finished_date,
        duration_seconds,
        folder,
        run_id,
        run_name
    ) VALUES (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
    )
    """
    con.execute(
        query,
        (
            run_info.project,
            run_info.pipeline_name,
            run_info.pipeline_id,
            run_info.repo_uri,
            run_info.repo_name,
            run_info.created_date,
            run_info.finished_date,
            run_info.duration_seconds,
            run_info.folder,
            run_info.run_id,
            run_info.run_name
        )
    )
