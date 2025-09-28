from src.data_fetcher import selenium_web
from src.data_transformer import process_csv_files
import pandas as pd



if __name__ == "__main__":
    #selenium_web(days=3650)
    process_csv_files(input_folder="/media/sacsresta/48F9473C7383F949/nepse/data", output_folder="/media/sacsresta/48F9473C7383F949/nepse/data_check")


