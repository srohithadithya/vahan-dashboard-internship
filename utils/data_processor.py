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
    
    df = df.sort_values(by=['Manufacturer', 'Vehicle_Type', 'Date'])

    df['YoY_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=12)
    df['QoQ_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=3)
    
    total_registrations_by_date = df.groupby('Date')['Registrations'].sum().reset_index()
    total_registrations_by_date['YoY_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=12)
    total_registrations_by_date['QoQ_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=3)

    df = pd.merge(df, total_registrations_by_date, on='Date', how='left', suffixes=('', '_Total_Calc'))
    df.rename(columns={'YoY_Growth_Total_Calc': 'YoY_Growth_Total', 'QoQ_Growth_Total_Calc': 'QoQ_Growth_Total'}, inplace=True)
    df.drop(columns=['Registrations_Total_Calc'], inplace=True)
    
    return df

def calculate_growth_metrics(df):
    """
    Calculates YoY and QoQ growth for registrations.
    This function is a wrapper for a pre-processed dataframe.
    """
    if df.empty:
        return df

    df['YoY_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=12)
    df['QoQ_Growth'] = df.groupby(['Manufacturer', 'Vehicle_Type'])['Registrations'].pct_change(periods=3)
    
    total_registrations_by_date = df.groupby('Date')['Registrations'].sum().reset_index()
    total_registrations_by_date['YoY_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=12)
    total_registrations_by_date['QoQ_Growth_Total'] = total_registrations_by_date['Registrations'].pct_change(periods=3)

    df = pd.merge(df, total_registrations_by_date, on='Date', how='left', suffixes=('', '_Total_Calc'))
    df.rename(columns={'YoY_Growth_Total_Calc': 'YoY_Growth_Total', 'QoQ_Growth_Total_Calc': 'QoQ_Growth_Total'}, inplace=True)
    df.drop(columns=['Registrations_Total_Calc'], inplace=True)
    
    return df

def calculate_market_share(df, date_range):
    """
    Calculates the market share for each manufacturer for a given date range.
    """
    if df.empty:
        return pd.DataFrame()

    start_date, end_date = date_range
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    total_registrations = filtered_df['Registrations'].sum()
    if total_registrations == 0:
        return pd.DataFrame()

    market_share_df = filtered_df.groupby('Manufacturer')['Registrations'].sum().reset_index()
    market_share_df['Market_Share'] = (market_share_df['Registrations'] / total_registrations) * 100
    
    return market_share_df.sort_values(by='Market_Share', ascending=False)

def main():
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
