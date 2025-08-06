import pandas as pd
import numpy as np
from datetime import date
import os

def generate_synthetic_vahan_data():
    """Generates a synthetic dataset for Vahan vehicle registrations."""
    start_date = date(2022, 1, 1)
    end_date = date.today()
    
    vehicle_types = ['2W', '3W', '4W']
    
    manufacturers = {
        '2W': ['Honda', 'Hero MotoCorp', 'TVS', 'Bajaj'],
        '3W': ['Bajaj Auto', 'Piaggio', 'Mahindra'],
        '4W': ['Maruti Suzuki', 'Hyundai', 'Tata Motors', 'Mahindra']
    }
    
    data = []
    current_date = start_date

    while current_date <= end_date:
        for vehicle_type in vehicle_types:
            for manufacturer in manufacturers[vehicle_type]:
                if vehicle_type == '2W':
                    registrations = np.random.randint(100000, 300000)
                elif vehicle_type == '4W':
                    registrations = np.random.randint(50000, 150000)
                else:
                    registrations = np.random.randint(5000, 20000)
                
                data.append([current_date, manufacturer, vehicle_type, registrations])

        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)

    df = pd.DataFrame(data, columns=['Date', 'Manufacturer', 'Vehicle_Type', 'Registrations'])
    return df

def main():
    """Main function to generate and save the synthetic data."""
    print("Generating synthetic Vahan data...")
    synthetic_df = generate_synthetic_vahan_data()
    
    raw_data_dir = 'data/raw'
    os.makedirs(raw_data_dir, exist_ok=True)
    
    file_path = os.path.join(raw_data_dir, 'vahan_data_raw.csv')
    synthetic_df.to_csv(file_path, index=False)
    
    print(f"Synthetic raw data saved to {file_path}")

if __name__ == "__main__":
    main()
