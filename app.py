import streamlit as st 
import pandas as pd
import matplotlib as plt 
import datetime


header = st.container()
dataset= st.container()
features = st.container()
visualization=st.container()
model_training = st.container()

with header:
    st.title("Store Sales Analysis")
    st.subheader("In this we build a Store sales prediction model using Regression")
    st.text("We analys data collected from the FAvorita Grocery store the year in 2013-2017")


with dataset:
    st.header("Favorita Grocery Store Sales Dataset")
    #st.text("This is the data analysis Section.")
    st.text("We look at the charecteritics of the data collected")
    data=pd.read_csv('New_Data.csv')
    data.set_index('id',inplace=True)
    #print(taxi_data.head()) // this will display the data in the console
    st.write(data.head())
    
with visualization:
    # Group by 'year' and 'month' and calculate the sum of 'sales'
    #monthly_sales = data.groupby(['Year', 'Month'])['sales'].sum().reset_index()
    #st.write("Sum of Sales by Month for each year")
    #st.bar_chart(monthly_sales)

    # Group by 'year' and 'month' and calculate the sum of 'sales'
    sales_sum_by_month = data.groupby(['Year', 'Month'])['sales'].sum().reset_index()
    sales_sum_by_year = data.groupby(['Year'])['sales'].sum().reset_index()    
# Display the result in Streamlit
    st.write("Sum of Sales by Month for Each Year:")
    st.write(sales_sum_by_month)
    st.subheader('Sum of Sales by Year')
    st.write(sales_sum_by_year)
    # Create separate bar charts for each year using Altair
    years = sorted(data['Year'].unique())
    for year in years:
        year_data = sales_sum_by_month[sales_sum_by_month['Year'] == year]
        st.subheader(f'Sum of sales for {year}')
        st.bar_chart(year_data.set_index('Month')['sales'])


with features:
    st.markdown("The Features that we created for our ML model training are ")




with model_training:
    st.header("We will use Logistic regression to train our Model  and use it to Predict our sales")
    #st.subheader('Month')
    sel_col, dis_col = st.columns(2)
    #Month=sel_col.slider('Select the Month', min_value=1, max_value=12,step=1)
    years = sorted(data['Year'].unique())

    # Year selection with st.selectbox
    selected_year = sel_col.selectbox("Select Year", years)

    # Month selection with st.slider
    selected_month = sel_col.slider("Select Month", 1, 12, 1)

    # Date selection with st.date_input
    selected_date = sel_col.date_input("Select Date", datetime.date(selected_year, selected_month, 1))

    #Select if Item in on promotion 
    Item_promotion = st.radio("Is the Item on Promotion ? ", ["YES", "NO"])


