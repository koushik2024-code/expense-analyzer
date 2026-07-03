# AI Expense Analyzer

An AI-powered expense tracking and analysis application built with Streamlit, pandas, and scikit-learn.

## Features
- **AI Classification**: Automatically categorizes your expenses based on transaction descriptions using NLP and Logistic Regression.
- **Spending Trends**: Visualizes monthly, weekly, and daily spending patterns with interactive Plotly charts.
- **Budget Recommendations**: Provides automated tips based on the distribution of your spending.
- **Financial Summary**: Gives a snapshot of total spent, average monthly spend, and your personal savings rate based on income.

## Setup

1. **Install Requirements**
   Ensure you have Python installed, then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the AI Model**
   Before running the app, train the initial classification model using the sample data:
   ```bash
   python train_model.py
   ```
   *This will generate a `classifier.pkl` inside the `models/` folder.*

3. **Run the Application**
   Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage
Once the app is running (usually accessible at `http://localhost:8501`), you can upload a CSV of your transactions to see your expense analysis. The CSV should contain the following columns:
- `date` (e.g. 2024-01-05)
- `description` (e.g. Swiggy order)
- `amount` (e.g. 320)
