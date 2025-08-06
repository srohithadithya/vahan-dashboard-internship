import plotly.express as px
import pandas as pd

def create_trend_chart(df, title, y_col, y_title):
    """
    Creates an interactive line chart showing registration trends over time.
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
    """
    if df.empty:
        return px.bar(title="No growth data to display")
    
    df = df.dropna(subset=[y_col])

    if df.empty:
        return px.bar(title="No growth data available for the selected period")

    df[y_col] = df[y_col] * 100

    fig = px.bar(df, x='Manufacturer', y=y_col, color='Vehicle_Type',
                 title=title,
                 labels={y_col: 'Growth (%)', 'Manufacturer': 'Manufacturer'},
                 barmode='group')
    fig.update_layout(xaxis_title="Manufacturer", yaxis_title="Growth (%)")
    return fig
