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

    Parameters
    ----------
    host : str
        Database host.
    port : int
        Database port.
    user : str
        Database user.
    password : str
        Database password.
    database : str, default 'tushare'
        Database name.

    Returns
    -------
    Engine
        SQLAlchemy Engine object.
    """
    # Replace 'your_database_url' with the actual database URL
    database_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(database_url, echo=False)


def _get_config(path: Path=CONFIG_PATH) -> dict:
    """
    Load database configuration from a JSON file.

    Parameters
    ----------
    path : Path, default CONFIG_PATH
        Path to the configuration file.

    Returns
    -------
    dict
        Dictionary containing database configuration.
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

    Parameters
    ----------
    path : Path, default CONFIG_PATH
        Path to the configuration file.

    Returns
    -------
    Engine
        SQLAlchemy Engine object.
    """
    config = _get_config(path)
    return _create_engine(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
