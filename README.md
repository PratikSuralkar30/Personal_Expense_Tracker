# Personal Expense Tracker with Data Visualization 💸

A comprehensive Python-based Personal Expense Tracker designed to clean, analyze, and visualize personal financial data. This project serves as a robust proof of work for Python Developer, Data Analyst, and Data Science roles.

## 📌 Project Overview
The Personal Expense Tracker automates the process of managing financial records. By taking raw transaction data (manual entries, CSV exports), it cleans the data, categorizes expenses, calculates key performance indicators (KPIs), and generates visual insights to help individuals understand their spending habits and improve their financial planning.

## 🎯 Problem Statement
Managing personal finances is challenging. Individuals often overspend because they lack visibility into where their money goes. Banks provide statements, but they lack advanced categorization, custom trend analysis, and actionable insights. This project solves that by transforming raw transaction logs into clear, visual financial summaries.

## 🏢 Industry Relevance
Financial literacy and personal analytics are core skills. This project demonstrates real-world data engineering and analytics skills:
- **Data Engineering**: Handling missing values, date parsing, data normalization.
- **Analytics**: Aggregation, feature engineering, trend calculation.
- **Visualization**: Storytelling with data using Matplotlib, Seaborn, and Streamlit.

## ✨ Features
- **Automated Data Generation**: Generates a synthetic financial dataset for easy testing.
- **Data Cleaning & Preprocessing**: Handles missing values, standardizes categories, and processes dates.
- **KPI Calculation**: Computes Total Spending, Average Transaction, and Highest Spending Categories.
- **Data Visualization**: Generates Bar charts, Line charts, and Pie charts using Matplotlib & Seaborn.
- **Interactive Dashboard**: A fully interactive Streamlit web application.
- **Report Generation**: Exports aggregated monthly and category-wise summaries to CSV.

## 🛠️ Tech Stack
- **Language**: Python 3.8+
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn, Plotly (for Streamlit)
- **Web Dashboard**: Streamlit

## 📂 Folder Structure
```text
Personal-Expense-Tracker/
│
├── data/               # Stores raw and processed CSV data
├── src/                # Core source code
│   ├── generate_data.py # Synthetic data generator
│   ├── process.py       # Data cleaning and KPI calculation
│   └── visualize.py     # Matplotlib/Seaborn charting functions
├── outputs/            # Final aggregated data 
├── images/             # Saved visualization charts (.png)
├── reports/            # Generated summary CSV reports
├── docs/               # Additional documentation
├── main.py             # CLI pipeline script
├── app.py              # Streamlit interactive dashboard
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Personal-Expense-Tracker
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the CLI Pipeline (Data Gen, Cleaning, Charts, Reports)
```bash
python main.py
```
*This will generate `data/expenses.csv`, save charts in `images/`, and create reports in `reports/`.*

### 4. Run the Interactive Streamlit Dashboard
```bash
streamlit run app.py
```
*This opens a local web server (typically http://localhost:8501) where you can interactively filter and view your expenses.*

## 📸 Sample Output
When you run the pipeline (`python main.py`), you will see the following terminal output:

```text
🚀 Starting Personal Expense Tracker Pipeline...
📊 Generating synthetic expense data...
✅ Generated 250 synthetic records at data/expenses.csv
🧹 Cleaning and processing data...
📈 Calculating key metrics...

========================================
📊 EXPENSE TRACKER SUMMARY
========================================
Total Spending:      $12,450.25
Total Transactions:  250
Average Transaction: $49.80
Highest Spending Category: Education ($3,450.00)
========================================

🎨 Generating visualizations...
✅ All visualizations saved in the 'images/' folder.
📄 Generating CSV summary reports...
✅ Reports saved in the 'reports/' folder.
🎉 Pipeline execution completed successfully!
```

### Screenshots to Capture
- Terminal output showing the KPIs.
- The interactive Streamlit Dashboard in the browser.
- The 4 generated charts in the `images/` folder.

## 🎓 Learning Outcomes
- Real-world application of **Pandas** for data wrangling.
- Modular code architecture separating data generation, processing, and visualization.
- Experience with **Streamlit** for rapid UI development.
- Generating automated financial reports.
