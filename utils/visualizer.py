import plotly.express as px
import pandas as pd

def create_trend_chart(df, title, y_col, y_title):
    """
    Creates an interactive line chart showing registration trends over time.

    Args:
        df (pd.DataFrame): The DataFrame to plot.
        title (str): The title of the chart.
        y_col (str): The column to be plotted on the y-axis (e.g., 'Registrations').
        y_title (str): The label for the y-axis.

    Returns:
        plotly.graph_objects.Figure: The Plotly figure object.
    """
    if df.empty:
        return px.line(title="No data available to display")

    fig = px.line(df, x='Date', y=y_col, color='Manufacturer',
                  title=title,
                  labels={'Date': 'Date', y_col: y_title},
                  line_shape='spline')
    fig.update_layout(xaxis_title='Date', yaxis_title=y_title, legend_title_text='Manufacturer',
                      hovermode="x unified")
    return fig

def create_market_share_pie_chart(df, date_range):
    """
    Creates a pie chart showing the market share of each manufacturer.

    Args:
        df (pd.DataFrame): The DataFrame containing market share data.
        date_range (tuple): The date range for the data.

    Returns:
        plotly.graph_objects.Figure: The Plotly figure object.
    """
    if df.empty:
        return px.pie(title="No data to display market share")

    title = f"Market Share by Manufacturer ({date_range[0].strftime('%b %Y')} to {date_range[1].strftime('%b %Y')})"
    fig = px.pie(df, values='Market_Share', names='Manufacturer',
                 title=title,
                 hover_data=['Registrations'],
                 labels={'Market_Share': 'Market Share (%)', 'Manufacturer': 'Manufacturer'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_growth_bar_chart(df, title, y_col):
    """
    Creates a bar chart showing YoY or QoQ growth rates.

    Args:
        df (pd.DataFrame): The DataFrame to plot.
        title (str): The title of the chart.
        y_col (str): The growth column to plot on the y-axis (e.g., 'YoY_Growth').

    Returns:
        plotly.graph_objects.Figure: The Plotly figure object.
    """
    if df.empty:
        return px.bar(title="No growth data to display")
    
    # Filter out NaNs from initial periods where growth can't be calculated
    df = df.dropna(subset=[y_col])

    # Convert growth from decimal to percentage for better visualization
    df[y_col] = df[y_col] * 100

    fig = px.bar(df, x='Manufacturer', y=y_col, color='Vehicle_Type',
                 title=title,
                 labels={y_col: 'Growth (%)', 'Manufacturer': 'Manufacturer'},
                 barmode='group')
    fig.update_layout(xaxis_title="Manufacturer", yaxis_title="Growth (%)")
    return fig