import requests
import pandas as pd
from io import StringIO
import os
import yfinance as yf
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress tracking

# URL to fetch Nifty 100 symbol list in CSV format
url = 'https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv'

# Headers with a modern User-Agent to avoid request blocks
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

# Send GET request to retrieve the CSV file
response = requests.get(url, headers=headers)
nifty100_raw_file = response.content

# Check if the request was successful
if response.status_code == 200:
    print('Data Fetched Successfully')
    
    # Load CSV content into a DataFrame
    df = pd.read_csv(StringIO(nifty100_raw_file.decode('utf-8')))
    
    # Extract the Nifty 100 symbols into a list
    try:
        nifty100_equity_symbols_list = df['Symbol'].to_list()
        print('Nifty100 Symbols saved:', nifty100_equity_symbols_list)
    except KeyError:
        print('Error: "Symbol" column not found in the DataFrame')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
else:
    print(f'Failed with Status Code: {response.status_code}')

# List of Nifty 100 tickers
nifty_100_tickers = nifty100_equity_symbols_list

def create_folder_structure():
    """
    Creates a folder structure based on the current year and month.
    This helps organize data files by year and month.
    
    Returns:
        str: Path of the month folder where data will be saved.
    """
    base_path = 'D:/Quantified Trader/Yfinance Data/Nifty100'
    current_year = datetime.now().strftime('%Y')
    current_month = datetime.now().strftime('%B')
    
    # Create base folder if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # Create year folder if it doesn't exist
    year_folder = os.path.join(base_path, current_year)
    if not os.path.exists(year_folder):
        os.makedirs(year_folder)
    
    # Create month subfolder if it doesn't exist
    month_folder = os.path.join(year_folder, current_month)
    if not os.path.exists(month_folder):
        os.makedirs(month_folder)
    
    return month_folder

def download_and_save_data(ticker, folder):
    """
    Downloads historical stock data for a given ticker and saves it as a CSV file.
    
    Args:
        ticker (str): Stock ticker symbol.
        folder (str): Path to the folder where CSV files will be saved.
    
    Returns:
        int: The number of rows saved to the file.
    """
    data = yf.download(ticker, interval="1m", period="max")
    
    if data.empty:
        print(f"No data found for {ticker}")
        return 0  # Return 0 rows if no data

    file_path = os.path.join(folder, f'{ticker}.csv')

    # Append new data to existing file if it exists
    if os.path.exists(file_path):
        existing_data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        new_data = data[~data.index.isin(existing_data.index)]
        if not new_data.empty:
            combined_data = pd.concat([existing_data, new_data]).sort_index()
        else:
            combined_data = existing_data
    else:
        combined_data = data.sort_index()  # No existing file, use downloaded data

    combined_data.to_csv(file_path)
    
    return len(combined_data)  # Return the number of rows saved

def main():
    """
    Main function to orchestrate data download and organization.
    It fetches data for all Nifty 100 stocks and saves them in the created folder structure.
    """
    folder = create_folder_structure()
    
    total_stocks = len(nifty_100_tickers)
    print(f'Total Nifty 100 Stocks: {total_stocks}')
    
    updated_stocks_count = 0
    updated_stock_details = {}

    for ticker in tqdm(nifty_100_tickers, desc="Downloading data", unit="stock"):
        rows_updated = download_and_save_data(ticker+'.NS', folder)
        if rows_updated > 0:
            updated_stocks_count += 1
            updated_stock_details[ticker] = rows_updated

    # Print summary of updates
    print(f'Total Stocks Updated: {updated_stocks_count}')
    for ticker, rows in updated_stock_details.items():
        print(f'{ticker}: {rows} rows updated.')

if __name__ == "__main__":
    main()
