import pandas as pd
import numpy as np
import os

def process_vahan_data(raw_data_path):
    """Loads raw data and calculates YoY and QoQ growth."""
    
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        print(f"Error: Raw data file not found at {raw_data_path}.")
        return pd.DataFrame()
        
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort data for correct calculations
    df = df.sort_values(by=['Manufacturer', 'Vehicle_Type', 'Date'])

    # Calculate YoY and QoQ growth for registrations
    df['YoY_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=12)
    df['QoQ_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=3)
    
    # For overall growth, first aggregate by date
    total_registrations_by_date = df.groupby('Date')['Registrations'].sum().reset_index()
    total_registrations_by_date['YoY_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=12)
    total_registrations_by_date['QoQ_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=3)

    # Merge total growth metrics back into the main DataFrame
    df = pd.merge(df, total_registrations_by_date, on='Date', how='left', suffixes=('', '_Total_Calc'))
    df.rename(columns={'YoY_Growth_Total_Calc': 'YoY_Growth_Total', 'QoQ_Growth_Total_Calc': 'QoQ_Growth_Total'}, inplace=True)
    df.drop(columns=['Registrations_Total_Calc'], inplace=True)
    
    return df

def main():
    """
    Main function to process the raw data and save the processed file.
    """
    raw_data_path = 'data/raw/vahan_data_raw.csv'
    
    if os.path.exists(raw_data_path):
        print("Processing raw data...")
        processed_df = process_vahan_data(raw_data_path)
        
        if not processed_df.empty:
            processed_data_dir = 'data/processed'
            os.makedirs(processed_data_dir, exist_ok=True)
            processed_file_path = os.path.join(processed_data_dir, 'vahan_data_processed.csv')
            processed_df.to_csv(processed_file_path, index=False)
            print(f"Processed data saved to {processed_file_path}")
        else:
            print("Processing failed. No data to save.")
    else:
        print(f"Raw data file not found at {raw_data_path}. Please run scrape_vahan_data.py first.")

if __name__ == "__main__":
    main()