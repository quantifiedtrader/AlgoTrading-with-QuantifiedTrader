import os
import pandas as pd

# Folder containing the CSV files
folder_path = "file_path"

# Loop through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Process only CSV files
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file
        file = pd.read_csv(file_path)
        
        # Create a new DataFrame to consolidate data
        new_file = pd.DataFrame()
        
        # Extract and align relevant columns
        new_file['datetime'] = file['Datetime']
        new_file['Open'] = file[[col for col in file.columns if 'Open' in str(col)]].bfill(axis=1).iloc[:, 0]
        new_file['High'] = file[[col for col in file.columns if 'High' in str(col)]].bfill(axis=1).iloc[:, 0]
        new_file['Low'] = file[[col for col in file.columns if 'Low' in str(col)]].bfill(axis=1).iloc[:, 0]
        new_file['Close'] = file[[col for col in file.columns if 'Close' in str(col)]].bfill(axis=1).iloc[:, 0]
        new_file['Adj Close'] = file[[col for col in file.columns if 'Adj Close' in str(col)]].bfill(axis=1).iloc[:, 0]
        new_file['Volume'] = file[[col for col in file.columns if 'Volume' in str(col)]].bfill(axis=1).iloc[:, 0]
        
        # Save the processed DataFrame back to the file
        new_file.to_csv(file_path, index=False)
        print(f"Processed and saved: {filename}")

print("All files processed!")