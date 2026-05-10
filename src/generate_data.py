import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_synthetic_data(num_records=200, output_path="data/expenses.csv"):
    """Generates synthetic expense data for testing the application."""
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    categories = {
        "Groceries": [20, 150],
        "Food & Dining": [10, 80],
        "Transport": [5, 50],
        "Bills & Utilities": [50, 200],
        "Shopping": [30, 300],
        "Entertainment": [15, 100],
        "Health": [20, 250],
        "Education": [50, 500]
    }
    
    payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash"]
    
    records = []
    
    # Generate dates for the last 90 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    
    for _ in range(num_records):
        # Random date
        random_days = random.randint(0, 90)
        tx_date = start_date + timedelta(days=random_days)
        
        # Random category and amount
        category = random.choice(list(categories.keys()))
        min_amt, max_amt = categories[category]
        amount = round(random.uniform(min_amt, max_amt), 2)
        
        # Random payment method
        payment_method = random.choice(payment_methods)
        
        # Description
        description = f"Payment for {category.lower()}"
        
        records.append({
            "Date": tx_date.strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
            "Payment_Method": payment_method,
            "Description": description
        })
        
    df = pd.DataFrame(records)
    df = df.sort_values(by="Date", ascending=False)
    df.to_csv(output_path, index=False)
    print(f"Generated {num_records} synthetic records at {output_path}")

if __name__ == "__main__":
    generate_synthetic_data()
