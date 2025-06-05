"""
Connect to local tushare database

Author: Yanzhong(Eric) Huang
"""

from pathlib import Path
from sqlalchemy import create_engine, Engine


CONFIG_PATH = Path("config.json")  # default database configuration file path


def _create_engine(host: str,
                   port: int,
                   user: str,
                   password: str,
                   database: str = "tushare") -> Engine:
    """
    Create a SQLAlchemy engine to connect to the local tushare mysql database.

    :param host: Database host
    :param port: Database port
    :param user: Database user
    :param password: Database password
    :param database: Database name, default is 'tushare'
    :return: SQLAlchemy Engine object
    """
    # Replace 'your_database_url' with the actual database URL
    database_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(database_url, echo=False)


def _get_config(path: Path=CONFIG_PATH) -> dict:
    """
    Load database configuration from a JSON file.

    :param path: Path to the configuration file
    :return: Dictionary containing database configuration
    """
    import json
    if not path.exists():
        raise FileNotFoundError(f"Configuration file {path} does not exist.")

    with open(path, encoding='utf-8') as f:
        config = json.load(f)

    return config["database"]


def get_engine(path: Path=CONFIG_PATH) -> Engine:
    """
    Get a SQLAlchemy engine using the configuration from a JSON file.

    :param path: Path to the configuration file
    :return: SQLAlchemy Engine object
    """
    config = _get_config(path)
    return _create_engine(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
