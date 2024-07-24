from src.data_fetcher import selenium_web
from src.data_transformer import process_csv_files
import pandas as pd

selenium_web(days=1000)
process_csv_files()


