import pandas as pd
import os

def load_processed_data(file_path='data/processed/vahan_data_processed.csv'):
    """
    Loads the pre-processed Vahan vehicle registration data from a CSV file.
    
    Args:
        file_path (str): The path to the processed data CSV file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame, or an empty DataFrame if the file is not found.
    """
    if not os.path.exists(file_path):
        print(f"Error: Processed data file not found at {file_path}. "
              "Please run the data generation and processing scripts first.")
        return pd.DataFrame()
        
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df
