"""
Update data module

Author: Yanzhong(Eric) Huang

Retrieve data from the database and update the local data files.
"""

from src.database import get_engine


def main() -> None:
    engine = get_engine()
    print(f"Connected to the database successfully.\n{engine.url}")


if __name__ == "__main__":
    from time import perf_counter

    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==============\nTime cost: {end - start:.2f} s \n or {(end - start) / 60:.2f} min")
