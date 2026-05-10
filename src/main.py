import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta
import os

sns.set_theme(style="whitegrid")

class ExpenseTracker:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.img_dir = os.path.join(self.base_dir, 'outputs', 'images')
        self.report_dir = os.path.join(self.base_dir, 'outputs', 'reports')
        
        for directory in [self.data_dir, self.img_dir, self.report_dir]:
            os.makedirs(directory, exist_ok=True)
            
        self.raw_data_path = os.path.join(self.data_dir, 'synthetic_expenses.csv')
        self.df = None

    def generate_synthetic_data(self, num_records=200):
        categories = ['Food & Dining', 'Transportation', 'Rent & Utilities', 'Entertainment', 'Shopping', 'Healthcare']
        methods = ['Credit Card', 'Debit Card', 'UPI', 'Cash']
        data = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=90)

        for _ in range(num_records):
            random_days = random.randint(0, 90)
            tx_date = start_date + timedelta(days=random_days)
            category = random.choice(categories)
            method = random.choice(methods)
            
            if category == 'Rent & Utilities':
                amount = round(random.uniform(2000, 15000), 2)
            elif category == 'Food & Dining':
                amount = round(random.uniform(100, 1500), 2)
            else:
                amount = round(random.uniform(50, 5000), 2)
                
            data.append([tx_date.strftime('%Y-%m-%d'), category, amount, method, f"Dummy {category} expense"])

        raw_df = pd.DataFrame(data, columns=['Date', 'Category', 'Amount', 'Payment_Method', 'Description'])
        raw_df.to_csv(self.raw_data_path, index=False)
        print(f"✅ Generated {num_records} synthetic expense records.")

    def load_and_clean_data(self):
        self.df = pd.read_csv(self.raw_data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month_Year'] = self.df['Date'].dt.to_period('M')
        self.df.dropna(inplace=True)
        print("✅ Data loaded and cleaned successfully.")

    def analyze_data(self):
        print("\n--- 📊 EXPENSE ANALYSIS ---")
        total_spend = self.df['Amount'].sum()
        print(f"Total Spending: ₹{total_spend:,.2f}")
        
        cat_group = self.df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        print(f"Highest Spending Category: {cat_group.index[0]} (₹{cat_group.iloc[0]:,.2f})")
        
        days_tracked = (self.df['Date'].max() - self.df['Date'].min()).days
        if days_tracked > 0:
            print(f"Average Daily Spending: ₹{total_spend / days_tracked:,.2f}")

    def generate_visualizations(self):
        print("✅ Generating Visualizations...")
        
        # 1. Bar Chart
        plt.figure(figsize=(10, 6))
        cat_data = self.df.groupby('Category')['Amount'].sum().sort_values()
        sns.barplot(x=cat_data.values, y=cat_data.index, palette='viridis')
        plt.title('Total Expenses by Category')
        plt.tight_layout()
        plt.savefig(os.path.join(self.img_dir, 'category_bar_chart.png'))
        plt.close()

        # 2. Line Chart
        plt.figure(figsize=(10, 5))
        monthly_data = self.df.groupby('Month_Year')['Amount'].sum().reset_index()
        monthly_data['Month_Year'] = monthly_data['Month_Year'].astype(str)
        sns.lineplot(data=monthly_data, x='Month_Year', y='Amount', marker='o', color='crimson')
        plt.title('Monthly Spending Trend')
        plt.tight_layout()
        plt.savefig(os.path.join(self.img_dir, 'monthly_trend_chart.png'))
        plt.close()

        # 3. Pie Chart
        plt.figure(figsize=(8, 8))
        method_data = self.df.groupby('Payment_Method')['Amount'].count()
        plt.pie(method_data, labels=method_data.index, autopct='%1.1f%%', startangle=140)
        plt.title('Transaction Count by Payment Method')
        plt.savefig(os.path.join(self.img_dir, 'payment_method_pie.png'))
        plt.close()

    def generate_report(self):
        report_path = os.path.join(self.report_dir, 'expense_summary.csv')
        summary_df = self.df.groupby('Category').agg(
            Total_Amount=('Amount', 'sum'),
            Transaction_Count=('Amount', 'count'),
            Average_Transaction=('Amount', 'mean')
        ).round(2).sort_values(by='Total_Amount', ascending=False)
        summary_df.to_csv(report_path)
        print(f"✅ Summary report generated at outputs/reports/expense_summary.csv")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.generate_synthetic_data()
    tracker.load_and_clean_data()
    tracker.analyze_data()
    tracker.generate_visualizations()
    tracker.generate_report()
