import streamlit as st
import pandas as pd
import plotly.express as px
from src.process import load_and_clean_data, generate_summary

st.set_page_config(page_title="Personal Expense Tracker", layout="wide", page_icon="💸")

st.title("💸 Personal Expense Tracker & Dashboard")

# Load Data
@st.cache_data
def get_data():
    try:
        return load_and_clean_data("data/expenses.csv")
    except FileNotFoundError:
        st.error("Data file not found. Please run 'python main.py' first to generate synthetic data.")
        return pd.DataFrame()

df = get_data()

if not df.empty:
    st.sidebar.header("Filters")
    
    # Month Filter
    months = sorted(df['Month'].unique().tolist())
    selected_months = st.sidebar.multiselect("Select Month(s)", months, default=months)
    
    # Category Filter
    categories = sorted(df['Category'].unique().tolist())
    selected_categories = st.sidebar.multiselect("Select Categories", categories, default=categories)
    
    # Filter Data
    filtered_df = df[
        (df['Month'].isin(selected_months)) & 
        (df['Category'].isin(selected_categories))
    ]
    
    # KPIs
    st.subheader("Key Performance Indicators")
    summary = generate_summary(filtered_df)
    
    if summary:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Spending", f"${summary['total_spending']:,.2f}")
        col2.metric("Total Transactions", f"{summary['total_transactions']}")
        col3.metric("Avg Transaction", f"${summary['avg_transaction']:,.2f}")
        col4.metric("Top Category", f"{summary['highest_category']}")
    
    st.markdown("---")
    
    # Charts using Plotly for interactivity
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Category-wise Spending")
        cat_df = filtered_df.groupby('Category')['Amount'].sum().reset_index()
        fig_cat = px.bar(cat_df, x='Category', y='Amount', color='Category', 
                         title="Total Spending by Category")
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col_chart2:
        st.subheader("Spending by Payment Method")
        pay_df = filtered_df.groupby('Payment_Method')['Amount'].sum().reset_index()
        fig_pay = px.pie(pay_df, names='Payment_Method', values='Amount', 
                         title="Payment Methods Distribution")
        st.plotly_chart(fig_pay, use_container_width=True)
        
    st.subheader("Daily Spending Trend")
    daily_df = filtered_df.groupby('Date')['Amount'].sum().reset_index()
    fig_daily = px.line(daily_df, x='Date', y='Amount', title="Daily Spending Over Time")
    st.plotly_chart(fig_daily, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Recent Transactions")
    st.dataframe(filtered_df.sort_values(by="Date", ascending=False).head(10))
