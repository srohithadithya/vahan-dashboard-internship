# **Vahan Dashboard**

## **Project Objective**

The objective of this project is to build a simple, interactive dashboard focused on vehicle registration data from an investor's perspective. The dashboard is built using Python with the Streamlit framework and is designed to be clean and investor-friendly. The core functionality includes visualizing Year-over-Year (YoY) and Quarter-over-Quarter (QoQ) growth for vehicle registrations.

## **Features**

This dashboard includes the following key features:

* **Interactive Filters**: Users can select a date range and filter data by specific vehicle categories (2W/3W/4W) and manufacturers.

* **Key Performance Indicators (KPIs)**: Prominent cards display overall total registrations, total YoY growth, total QoQ growth, and the top-performing manufacturer for the selected period.  
* **Trend Analysis**: A line graph shows monthly vehicle registration trends over time for different manufacturers, allowing for easy comparison.

* **Growth Visualization**: Bar charts provide a clear view of YoY and QoQ growth rates for each manufacturer, helping to identify top performers and laggards.

* **Market Share Analysis**: A pie chart visualizes the market share of each manufacturer for the selected date range.

## **Technical Stack**

* **Language**: Python 3.12.0  
* **Dashboard Framework**: Streamlit  
* **Data Processing**: Pandas  
* **Visualization**: Plotly  
* **Version Control**: Git/GitHub

## **Setup Instructions**

To run this project locally, follow these steps:

1. **Clone the Repository**:  
   git clone https://github.com/your-username/dashboard-project.git  
   cd dashboard-project

2. **Create and Activate a Virtual Environment**:  
   python \-m venv venv  
   \# On Windows  
   .\\venv\\Scripts\\activate  
   \# On macOS/Linux  
   source venv/bin/activate

3. **Install Required Libraries**:  
   pip install \-r requirements.txt

4. Generate the Dataset:  
   Since a public dataset download is not available from the Vahan Dashboard, this project uses a script to generate a synthetic dataset that mimics the structure of the required data. This step must be performed first to create the necessary CSV files.

   python scripts/scrape\_vahan\_data.py

5. Process the Raw Data:  
   Next, process the raw data to calculate YoY and QoQ growth metrics.  
   python utils/data\_processor.py

6. Run the Dashboard:  
   With the data files now in the data/ folder, you can start the Streamlit application.  
   streamlit run app.py

   The dashboard will open in your default web browser at http://localhost:8501.

## **Data Assumptions**

* **Data Source**: The data is assumed to be a public dataset from the Vahan Dashboard, as required by the assignment.

* **Synthetic Data**: Due to the unavailability of a direct download link, the dataset used in this project is synthetically generated to simulate real-world vehicle registration data. The script scripts/scrape\_vahan\_data.py creates this data.  
* **Monthly Granularity**: The synthetic data is generated with a monthly frequency, which is sufficient for calculating both Year-over-Year (YoY) and Quarter-over-Quarter (QoQ) growth.  
* **Registration Count**: The Registrations column is assumed to represent the total number of vehicles registered for a given manufacturer, vehicle type, and month.

## **Feature Roadmap**

If this project were to be continued, the following features would be considered:

* **Live Data Integration**: Replace the synthetic data with a real-time data source by implementing a proper web scraping solution or an API call to the Vahan Dashboard.  
* **Geographical Analysis**: Add a map visualization to show vehicle registrations and growth by state or district.  
* **Advanced Analytics**: Incorporate a simple forecasting model to predict future registration trends, providing additional investment insights.  
* **Enhanced UI/UX**: Introduce custom theming, improved responsiveness for different screen sizes, and more detailed tooltips for all visualizations.  
* **User Authentication**: Implement a simple login system to protect the dashboard if it were to contain more sensitive data.

## **Submission Details**

* **Video Walkthrough**: A short screen recording (max 5 minutes) is available at the following link: \[Insert YouTube/Drive Link Here\]  
* **Key Insights from the Video**: The video explains what was built, how to use the dashboard, and key investor insights discovered from the data.  
