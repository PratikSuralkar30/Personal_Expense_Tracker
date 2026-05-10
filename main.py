import os
import pandas as pd
from src.generate_data import generate_synthetic_data
from src.process import load_and_clean_data, generate_summary
from src.visualize import (
    plot_category_spending, 
    plot_monthly_trend, 
    plot_payment_methods, 
    plot_daily_trend,
    save_plot
)

def main():
    print("Starting Personal Expense Tracker Pipeline...")
    
    # Phase 1: Generate Data if not exists
    data_path = "data/expenses.csv"
    if not os.path.exists(data_path):
        print("Generating synthetic expense data...")
        generate_synthetic_data(num_records=250, output_path=data_path)
    
    # Phase 2: Load and Clean Data
    print("Cleaning and processing data...")
    df = load_and_clean_data(data_path)
    
    # Phase 3: Generate Summary KPI
    print("Calculating key metrics...")
    summary = generate_summary(df)
    
    print("\n" + "="*40)
    print("EXPENSE TRACKER SUMMARY")
    print("="*40)
    print(f"Total Spending:      ${summary['total_spending']:,.2f}")
    print(f"Total Transactions:  {summary['total_transactions']}")
    print(f"Average Transaction: ${summary['avg_transaction']:,.2f}")
    print(f"Highest Spending Category: {summary['highest_category']} (${summary['highest_category_amount']:,.2f})")
    print("="*40 + "\n")
    
    # Phase 4: Data Visualization
    print("Generating visualizations...")
    
    fig_cat = plot_category_spending(df)
    save_plot(fig_cat, "category_spending.png")
    
    fig_month = plot_monthly_trend(df)
    save_plot(fig_month, "monthly_trend.png")
    
    fig_pay = plot_payment_methods(df)
    save_plot(fig_pay, "payment_methods.png")
    
    fig_daily = plot_daily_trend(df)
    save_plot(fig_daily, "daily_trend.png")
    
    print("All visualizations saved in the 'images/' folder.")
    
    # Phase 5: Report Generation
    print("Generating CSV summary reports...")
    os.makedirs("reports", exist_ok=True)
    
    # Category summary
    cat_summary = df.groupby('Category')['Amount'].sum().reset_index()
    cat_summary.to_csv("reports/category_summary.csv", index=False)
    
    # Monthly summary
    monthly_summary = df.groupby('Month')['Amount'].sum().reset_index()
    monthly_summary.to_csv("reports/monthly_summary.csv", index=False)
    
    print("Reports saved in the 'reports/' folder.")
    print("Pipeline execution completed successfully!")

if __name__ == "__main__":
    main()
