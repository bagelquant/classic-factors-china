# Data

This section provides an overview of a description of the data used in the project, including its source, structure, and any preprocessing steps taken.

## Data Source

**Tushare**: A comprehensive data provider for the Chinese financial market, covering stock prices, financial statements, and other market data. [Tushare](https://tushare.pro)

Data will be obtained using [bagel-tushare](https://github.com/bagelquant/bagel-tushare) package, a Python wrapper for Tushare that simplifies data retrieval and manipulation. Retrieved data will be stored in a local MySQL database for efficient access and analysis.

This project will provide a `database` module that retrieves data from local MySQL database and save it into `data` directory in the project root. The data will be stored in CSV format for easy access and manipulation.

All analysis will be performed using the data stored in the `data` directory. (For simplicity)
