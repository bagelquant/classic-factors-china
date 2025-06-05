"""
Retrieves data from the database.

Author: Yanzhong(Eric) Huang

- stock_basic
- daily
- book
"""

import pandas as pd
from sqlalchemy import Engine
from typing import Iterable


def get_stock_basic(engine: Engine) -> pd.DataFrame:
    """
    Retrieve stock basic data from the database.
    :param engine: database engine object
    """
    query = """
            SELECT * FROM stock_basic
            WHERE market = '主板'
            ORDER BY ts_code
            """
    return pd.read_sql(query, engine, parse_dates=["list_date", "delist_date"], index_col="ts_code")


def get_daily(engine: Engine,
              ts_codes: Iterable[str]) -> pd.DataFrame:
    """
    Retrieve daily stock data from the database.
    :param engine: database engine object
    :param ts_codes: iterable of stock codes to filter the data
    """
    query = f"""
            SELECT * FROM daily
            WHERE ts_code IN {tuple(ts_codes) if ts_codes else '()'}
            ORDER BY ts_code, trade_date
            """
    return pd.read_sql(query, engine, parse_dates=["trade_date"], index_col=["ts_code", "trade_date"])


def get_adj_factor(engine: Engine,
                   ts_codes: Iterable[str]) -> pd.DataFrame:
    """
    Retrieve adjusted factor data from the database.
    :param engine: database engine object
    :param ts_codes: iterable of stock codes to filter the data
    """
    query = f"""
            SELECT * FROM adj_factor
            WHERE ts_code IN {tuple(ts_codes) if ts_codes else '()'}
            ORDER BY ts_code, trade_date
            """
    return pd.read_sql(query, engine, parse_dates=["trade_date"], index_col=["ts_code", "trade_date"])


def get_fundamental(engine: Engine,
                     table_name: str,
                     columns: Iterable[str],
                     ts_codes: Iterable[str]) -> pd.DataFrame:
    """
    Retrieve fundamental data from the database.
    :param engine: database engine object
    :param table_name: name of the fundamental table
    :param columns: iterable of column names to select
    :param ts_codes: iterable of stock codes to filter the data
    """
    query = f"""
            SELECT ts_code, f_ann_date, {', '.join(columns)} FROM {table_name}
            WHERE ts_code IN {tuple(ts_codes) if ts_codes else '()'}
            ORDER BY ts_code, f_ann_date
            """
    df = pd.read_sql(query, engine, parse_dates=["f_ann_date"], index_col=["ts_code", "f_ann_date"])
    # change f_ann_date index name to trade_date
    df.index.names = ["ts_code", "trade_date"]
    return df
