import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set seaborn style for better aesthetics
sns.set_theme(style="whitegrid")

def save_plot(fig, filename):
    """Utility to save plots to the images directory."""
    os.makedirs("images", exist_ok=True)
    filepath = os.path.join("images", filename)
    fig.savefig(filepath, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return filepath

def plot_category_spending(df):
    """Generates a bar chart for category-wise spending."""
    category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_totals.values, y=category_totals.index, ax=ax, palette="viridis")
    
    ax.set_title("Total Spending by Category", fontsize=16, fontweight='bold')
    ax.set_xlabel("Amount ($)", fontsize=12)
    ax.set_ylabel("Category", fontsize=12)
    
    return fig

def plot_monthly_trend(df):
    """Generates a line chart for monthly spending trend."""
    monthly_totals = df.groupby('Month')['Amount'].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=monthly_totals, x='Month', y='Amount', marker='o', linewidth=2, color='coral', ax=ax)
    
    ax.set_title("Monthly Spending Trend", fontsize=16, fontweight='bold')
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Total Spending ($)", fontsize=12)
    plt.xticks(rotation=45)
    
    return fig

def plot_payment_methods(df):
    """Generates a pie chart for payment methods."""
    method_totals = df.groupby('Payment_Method')['Amount'].sum()
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(method_totals.values, labels=method_totals.index, autopct='%1.1f%%', 
           startangle=140, colors=sns.color_palette("pastel"))
    ax.set_title("Spending by Payment Method", fontsize=16, fontweight='bold')
    
    return fig

def plot_daily_trend(df):
    """Generates a daily spending line chart."""
    daily_totals = df.groupby('Date')['Amount'].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=daily_totals, x='Date', y='Amount', color='teal', linewidth=1, ax=ax)
    
    ax.set_title("Daily Spending Trend", fontsize=16, fontweight='bold')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Amount ($)", fontsize=12)
    
    return fig
