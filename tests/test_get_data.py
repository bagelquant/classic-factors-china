"""
Test suite for testing data retrieval functions from the database.

Author: Yanzhong(Eric) Huang
"""

from unittest import TestCase
from src.database import get_engine
from src.database import get_stock_basic, get_daily, get_adj_factor, get_fundamental


class TestGetData(TestCase):

    def setUp(self) -> None:
        """Set up the test case by initializing the database engine."""
        self.engine = get_engine()

    def test_get_stock_basic(self) -> None:
        print("\n======Testing get_stock_basic function======")
        stock_basic = get_stock_basic(self.engine)
        print(stock_basic)

    def test_get_daily(self) -> None:
        print("\n======Testing get_daily function======")
        daily_data = get_daily(self.engine, ts_codes=["000001.SZ", "600000.SH"])
        print(daily_data)

    def test_get_adj_factor(self) -> None:
        print("\n======Testing get_adj_factor function======")
        adj_factor_data = get_adj_factor(self.engine, ts_codes=["000001.SZ", "600000.SH"])
        print(adj_factor_data)

    def test_get_fundamental(self) -> None:
        print("\n======Testing get_fundamental function======")
        fundamental_data = get_fundamental(self.engine,
                                           table_name="income",
                                           columns=["total_revenue", "basic_eps"],
                                           ts_codes=["000001.SZ", "600000.SH"])
        print(fundamental_data)
