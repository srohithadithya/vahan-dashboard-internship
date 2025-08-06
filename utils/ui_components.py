import streamlit as st
import pandas as pd

def display_kpi_card(title, value, delta=None):
    """
    Displays a custom KPI card with a title, a main value, and an optional delta.

    Args:
        title (str): The title of the KPI card.
        value (any): The main value to display.
        delta (str, optional): The change or difference to display. Defaults to None.
    """
    with st.container():
        st.markdown(
            f"""
            <div style="
                border: 1px solid #e6e6e6;
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
                background-color: #f9f9f9;
                text-align: center;
            ">
                <p style="font-size: 14px; color: #888; margin: 0;">{title}</p>
                <h3 style="font-size: 28px; color: #333; margin: 5px 0;">{value}</h3>
                <p style="font-size: 12px; color: green; margin: 0;">{delta}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def create_filters(df):
    """
    Creates the Streamlit sidebar filters for the dashboard.

    Args:
        df (pd.DataFrame): The main DataFrame to get filter options from.

    Returns:
        tuple: A tuple containing the selected date range, manufacturers, and vehicle types.
    """
    if df.empty:
        return (None, None), [], []
        
    st.sidebar.header("Dashboard Filters")
    
    # Date Range Selection
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date))
    
    # Manufacturer Filter
    all_manufacturers = sorted(df['Manufacturer'].unique().tolist())
    selected_manufacturers = st.sidebar.multiselect(
        "Select Manufacturer(s)",
        options=all_manufacturers,
        default=all_manufacturers
    )
    
    # Vehicle Type Filter
    all_vehicle_types = sorted(df['Vehicle_Type'].unique().tolist())
    selected_vehicle_types = st.sidebar.multiselect(
        "Select Vehicle Type(s)",
        options=all_vehicle_types,
        default=all_vehicle_types
    )
    
    return date_range, selected_manufacturers, selected_vehicle_types