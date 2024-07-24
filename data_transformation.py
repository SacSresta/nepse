import os
import pandas as pd

# Define the path to the folder containing the CSV files
folder_path = r'C:\Users\sachi\OneDrive\Documents\SELENIUM\data'

# List all files in the folder
files = os.listdir(folder_path)

# Filter the list to include only CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Dictionary to store DataFrames for each symbol
symbol_dataframes = {}

# Iterate over the list of CSV files and read each one into a DataFrame
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    
    # Extract the date from the filename (assuming format is data_YYYY_MM_DD.csv)
    date_str = csv_file.split('_')[1] + '-' + csv_file.split('_')[2] + '-' + csv_file.split('_')[3].split('.')[0]
    
    # Add the date column to the DataFrame
    df['Date'] = date_str
    
    # Iterate over unique symbols in the current DataFrame
    for symbol in df['Symbol'].unique():
        symbol_df = df[df['Symbol'] == symbol]
        
        # If the symbol is already in the dictionary, append the new data
        if symbol in symbol_dataframes:
            symbol_dataframes[symbol] = pd.concat([symbol_dataframes[symbol], symbol_df])
        else:
            symbol_dataframes[symbol] = symbol_df

# Display the DataFrame for each symbol
for symbol, df in symbol_dataframes.items():
    print(f"Data for symbol {symbol}:")
    print(df)
    print("\n")

# Optionally, save each symbol DataFrame to a separate CSV file
for symbol, df in symbol_dataframes.items():
    output_path = os.path.join(folder_path, f"{symbol}_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Data for symbol {symbol} saved to {output_path}")
