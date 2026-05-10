import pandas as pd
import os

def load_and_clean_data(file_path="data/expenses.csv"):
    """Loads CSV data, cleans it, and prepares it for analysis."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}. Please generate data first.")
        
    df = pd.read_csv(file_path)
    
    # Drop rows with missing Amount or Date
    df = df.dropna(subset=['Amount', 'Date'])
    
    # Convert Date to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Add Year-Month column for monthly analysis
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    
    # Clean up categories and payment methods (strip whitespace, title case)
    df['Category'] = df['Category'].astype(str).str.strip().str.title()
    df['Payment_Method'] = df['Payment_Method'].astype(str).str.strip().str.title()
    
    # Ensure amount is numeric
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0.0)
    
    return df

def generate_summary(df):
    """Calculates key performance indicators (KPIs) from the cleaned data."""
    if df.empty:
        return {}
        
    total_spending = df['Amount'].sum()
    total_transactions = len(df)
    avg_transaction = total_spending / total_transactions if total_transactions > 0 else 0
    
    highest_category = df.groupby('Category')['Amount'].sum().idxmax()
    highest_category_amount = df.groupby('Category')['Amount'].sum().max()
    
    return {
        "total_spending": total_spending,
        "total_transactions": total_transactions,
        "avg_transaction": avg_transaction,
        "highest_category": highest_category,
        "highest_category_amount": highest_category_amount
    }
