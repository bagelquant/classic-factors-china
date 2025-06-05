"""
Update data module

Author: Yanzhong(Eric) Huang

Retrieve data from the database and update the local data files.
"""

from pathlib import Path
from src.database import get_engine
from src.database import get_stock_basic, get_daily, get_adj_factor, get_fundamental

OUTPUT_PATH = Path("data/")
BALANCESHEET_COLS = [
    "total_share"
]
INCOME_COLS = [
    "total_revenue",
    "basic_eps"
]
CASHFLOW_COLS = [
    "net_profit",
]


def main() -> None:
    engine = get_engine()
    print(f"Connected to the database successfully.\n{engine.url}")

    print("=" * 20 + "\nRetrieving stock basic data...")
    stock_basic = get_stock_basic(engine)
    stock_basic.to_csv(OUTPUT_PATH / "stock_list.csv")
    stock_list: list[str] = stock_basic.index.tolist()

    print("=" * 20 + "\nRetrieving daily data...")
    daily_data = get_daily(engine, ts_codes=stock_list)
    daily_data.to_csv(OUTPUT_PATH / "daily.csv")

    print("=" * 20 + "\nRetrieving adjusted factor data...")
    adj_factor_data = get_adj_factor(engine, ts_codes=stock_list)
    adj_factor_data.to_csv(OUTPUT_PATH / "adj_factor.csv")

    print("=" * 20 + "\nRetrieving balancesheet data...")
    balancesheet_data = get_fundamental(engine,
                                        table_name="balancesheet",
                                        columns=BALANCESHEET_COLS,
                                        ts_codes=stock_list)
    balancesheet_data.to_csv(OUTPUT_PATH / "balancesheet.csv")

    print("=" * 20 + "\nRetrieving income data...")
    income_data = get_fundamental(engine,
                                  table_name="income",
                                  columns=INCOME_COLS,
                                  ts_codes=stock_list)
    income_data.to_csv(OUTPUT_PATH / "income.csv")

    print("=" * 20 + "\nRetrieving cashflow data...")
    cashflow_data = get_fundamental(engine,
                                    table_name="cashflow",
                                    columns=CASHFLOW_COLS,
                                    ts_codes=stock_list)
    cashflow_data.to_csv(OUTPUT_PATH / "cashflow.csv")


if __name__ == "__main__":
    from time import perf_counter

    start = perf_counter()
    main()
    end = perf_counter()
    print("\n" + "=" * 20)
    print(f"Time cost: {end - start:.2f} s \n or {(end - start) / 60:.2f} min")
