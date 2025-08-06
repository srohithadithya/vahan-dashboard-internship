import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_processed_data
from utils.data_processor import calculate_growth_metrics, calculate_market_share
from utils.visualizer import create_trend_chart, create_market_share_pie_chart, create_growth_bar_chart
from utils.ui_components import display_kpi_card, create_filters

st.set_page_config(
    page_title="Vahan Dashboard for Investors",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Vehicle Registration Dashboard")
st.markdown("A data-driven dashboard for investors to analyze vehicle registration trends, built using Streamlit.")

@st.cache_data
def get_data():
    df = load_processed_data()
    if df.empty:
        return df
    
    df = calculate_growth_metrics(df)
    return df

data = get_data()

if data.empty:
    st.warning("Data could not be loaded. Please ensure the data generation and processing scripts have been run.")
    st.stop()

date_range, selected_manufacturers, selected_vehicle_types = create_filters(data)

st.header("Key Investor Insights")

filtered_data = data[
    (data['Date'] >= date_range[0]) &
    (data['Date'] <= date_range[1]) &
    (data['Manufacturer'].isin(selected_manufacturers)) &
    (data['Vehicle_Type'].isin(selected_vehicle_types))
]

if filtered_data.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

st.subheader("Performance Overview")
col1, col2, col3, col4 = st.columns(4)

total_registrations = filtered_data['Registrations'].sum()
yoy_growth_total = filtered_data['YoY_Growth_Total'].iloc[-1] if 'YoY_Growth_Total' in filtered_data.columns and not filtered_data['YoY_Growth_Total'].empty else np.nan
qoq_growth_total = filtered_data['QoQ_Growth_Total'].iloc[-1] if 'QoQ_Growth_Total' in filtered_data.columns and not filtered_data['QoQ_Growth_Total'].empty else np.nan
top_manufacturer = filtered_data.groupby('Manufacturer')['Registrations'].sum().idxmax()

with col1:
    display_kpi_card("Total Registrations", f"{total_registrations:,}")
with col2:
    yoy_delta = f"{yoy_growth_total:.2%}" if not pd.isna(yoy_growth_total) else "N/A"
    display_kpi_card("Overall YoY Growth", yoy_delta)
with col3:
    qoq_delta = f"{qoq_growth_total:.2%}" if not pd.isna(qoq_growth_total) else "N/A"
    display_kpi_card("Overall QoQ Growth", qoq_delta)
with col4:
    display_kpi_card("Top Manufacturer", top_manufacturer)

st.markdown("---")

st.subheader("Registration Trends Over Time")
trend_chart = create_trend_chart(filtered_data, "Monthly Vehicle Registrations", 'Registrations', 'Number of Registrations')
st.plotly_chart(trend_chart, use_container_width=True)

st.subheader("Growth Analysis")
growth_col1, growth_col2 = st.columns(2)

with growth_col1:
    yoy_chart = create_growth_bar_chart(filtered_data, "Year-over-Year Growth by Manufacturer", 'YoY_Growth')
    st.plotly_chart(yoy_chart, use_container_width=True)

with growth_col2:
    qoq_chart = create_growth_bar_chart(filtered_data, "Quarter-over-Quarter Growth by Manufacturer", 'QoQ_Growth')
    st.plotly_chart(qoq_chart, use_container_width=True)

st.subheader("Market Share Analysis")
market_share_df = calculate_market_share(filtered_data, date_range)
market_share_chart = create_market_share_pie_chart(market_share_df, date_range)
st.plotly_chart(market_share_chart, use_container_width=True)
