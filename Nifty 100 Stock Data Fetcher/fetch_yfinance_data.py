import os
import requests
import yfinance as yf
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from io import StringIO

# URLs to fetch Nifty 100 and Nifty 200 symbols
urls = {
    "Nifty100": 'https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv',
    "Nifty200": 'https://nsearchives.nseindia.com/content/indices/ind_nifty200list.csv'
}

# Headers with a modern User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

# Function to fetch symbols list from a URL
def fetch_symbols(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        raw_file = response.content
        df = pd.read_csv(StringIO(raw_file.decode('utf-8')))
        return df['Symbol'].to_list()
    else:
        print(f"Failed to fetch data from {url}, status code: {response.status_code}")
        return []

# Get the Nifty 100 and Nifty 200 symbols
nifty100_symbols = fetch_symbols(urls["Nifty100"])
nifty200_symbols = fetch_symbols(urls["Nifty200"])

# Function to create folder structure
def create_folder_structure(index_name):
    base_path = f'D:/Quantified Trader/Yfinance Data/{index_name}'
    current_year = datetime.now().strftime('%Y')
    current_month = datetime.now().strftime('%B')
    
    # Create folders
    year_folder = os.path.join(base_path, current_year)
    month_folder = os.path.join(year_folder, current_month)
    os.makedirs(month_folder, exist_ok=True)
    
    return month_folder

# Function to download and save stock data
def download_and_save_data(ticker, folder):
    data = yf.download(ticker, interval="1m", period="max",multi_level_index=False)
    
    if data.empty:
        print(f"No data found for {ticker}")
        return 0

    file_path = os.path.join(folder, f'{ticker}.csv')
    
    if os.path.exists(file_path):
        existing_data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        new_data = data[~data.index.isin(existing_data.index)]
        combined_data = pd.concat([existing_data, new_data]).sort_index() if not new_data.empty else existing_data
    else:
        combined_data = data.sort_index()

    combined_data.to_csv(file_path)
    return len(combined_data)

# Main function to process both Nifty 100 and Nifty 200
def main():
    for index_name, symbols in [("Nifty100", nifty100_symbols), ("Nifty200", nifty200_symbols)]:
        folder = create_folder_structure(index_name)
        
        total_stocks = len(symbols)
        print(f'Total {index_name} Stocks: {total_stocks}')
        
        updated_stocks_count = 0
        updated_stock_details = {}

        for ticker in tqdm(symbols, desc=f"Downloading data for {index_name}", unit="stock"):
            rows_updated = download_and_save_data(ticker + '.NS', folder)
            if rows_updated > 0:
                updated_stocks_count += 1
                updated_stock_details[ticker] = rows_updated

        print(f'Total {index_name} Stocks Updated: {updated_stocks_count}')
        for ticker, rows in updated_stock_details.items():
            print(f'{ticker}: {rows} rows updated.')

if __name__ == "__main__":
    main()
