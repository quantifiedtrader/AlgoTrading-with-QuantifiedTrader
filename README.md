# Nifty 100 Stock Data Fetcher

This project is a Python script for downloading historical minute-by-minute stock data for Nifty 100 companies from Yahoo Finance. It fetches the latest list of Nifty 100 stocks from the NSE India website, organizes the downloaded data by year and month, and saves it as CSV files for each stock. This can be useful for stock market analysis, backtesting trading strategies, or portfolio analysis.

## Features

- **Fetches Nifty 100 stock symbols** directly from NSE India.
- **Downloads minute-level stock data** from Yahoo Finance for all symbols.
- **Organizes data in a structured folder format** by year and month.
- **Appends new data** to existing CSV files, ensuring that data is up-to-date.

## Requirements

Ensure you have Python 3.7+ installed, along with the following libraries:
- `requests`
- `pandas`
- `yfinance`
- `tqdm`

Install the dependencies using:
```pip install requests pandas yfinance tqdm```

## Usage
Download the repository: Clone the repository or download the ZIP file:


```git clone https://github.com/yourusername/nifty-100-stock-fetcher.git```

```cd nifty-100-stock-fetcher```

Run the script: Execute the script to download and save Nifty 100 stock data:


```python nifty_100_data_fetcher.py```

Folder Structure: The downloaded data will be saved in D:/Quantified Trader/Yfinance Data/Nifty100, organized by:


Year (e.g., 2023)

Month (e.g., August)

Each stock's data will be saved as a CSV file with the stock symbol as the filename.

Project Structure

```
├── nifty_100_data_fetcher.py     # Main script to run the data fetching process
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore file
```



## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

NSE India for providing the list of Nifty 100 stocks.
Yahoo Finance for providing historical stock data.


