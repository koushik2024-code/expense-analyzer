import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd

from src.data_processor   import DataProcessor
from src.nlp_engine       import NLPEngine
from src.ml_classifier    import ExpenseClassifier
from src.predictor        import Predictor
from src.report_generator import ReportGenerator
from src.visualizer       import Visualizer

MODEL_PATH = 'models/classifier.pkl'

@st.cache_resource
def load_or_train_model():
    import os
    from src.data_processor import DataProcessor
    from src.nlp_engine     import NLPEngine
    from src.ml_classifier  import ExpenseClassifier
    import pandas as pd
    nlp = NLPEngine()
    clf = ExpenseClassifier()
    if os.path.exists(MODEL_PATH):
        clf.load(MODEL_PATH)
    else:
        st.info('Training AI model for the first time, please wait...')
        dp = DataProcessor()
        df = dp.load('data/sample_data.csv')
        X  = nlp.preprocess_series(df['description'])
        y  = df['category']
        clf.train(X, y)
        os.makedirs('models', exist_ok=True)
        clf.save(MODEL_PATH)
    return nlp, clf

st.set_page_config(page_title='AI Expense Analyzer', layout='wide')
st.title('AI-Powered Expense Analyzer')
st.markdown('Upload your transaction CSV and get instant AI-driven insights.')

st.sidebar.header('Settings')
uploaded = st.sidebar.file_uploader('Upload Transactions CSV', type=['csv'])
income   = st.sidebar.number_input('Your Monthly Income (Rs)', value=50000, step=1000)
use_ai   = st.sidebar.checkbox('Use AI to auto-classify categories', value=True)

if uploaded is None:
    st.info('Upload a CSV file from the sidebar to begin.')
    st.markdown('**Expected CSV columns:** date, description, amount')
    st.code('date,description,amount\n2024-01-05,Swiggy order,320\n2024-01-06,Ola cab,150')
    st.stop()

dp = DataProcessor()
df = dp.clean(pd.read_csv(uploaded))

if use_ai:
    nlp, clf = load_or_train_model()
    X = nlp.preprocess_series(df['description'])
    df['category'] = clf.predict(X)
    st.sidebar.success('AI classification applied')
elif 'category' not in df.columns:
    st.sidebar.warning('Enable AI classification or upload CSV with a category column.')

pred = Predictor()
vis  = Visualizer()
rep  = ReportGenerator()

savings = pred.savings_analysis(df, income)
tips    = pred.budget_recommendations(df)

st.subheader('Overview')
c1, c2, c3, c4 = st.columns(4)
c1.metric('Total Spent',       f"Rs {savings['total_spent']:,}")
c2.metric('Avg Monthly Spend', f"Rs {savings['avg_monthly']:,}")
c3.metric('Savings Rate',      f"{savings['savings_rate_%']}%")
c4.metric('Top Category',      savings['top_category'])

st.markdown('---')
st.subheader('Spending Trends')
col1, col2 = st.columns(2)
col1.plotly_chart(vis.monthly_bar(pred.monthly_trend(df)),   use_container_width=True)
col2.plotly_chart(vis.category_pie(pred.category_split(df)), use_container_width=True)

col3, col4 = st.columns(2)
col3.plotly_chart(vis.daily_line(df),                        use_container_width=True)
col4.plotly_chart(vis.daywise_bar(pred.daywise_trend(df)),   use_container_width=True)

st.plotly_chart(vis.category_bar(pred.category_split(df)),   use_container_width=True)

st.markdown('---')
col5, col6 = st.columns(2)
with col5:
    st.subheader('Financial Summary')
    st.text(rep.generate_text_summary(savings))
with col6:
    st.subheader('Budget Recommendations')
    for tip in tips:
        st.info(tip)

st.markdown('---')
st.subheader('Detailed Data')
with st.expander('Top 10 Highest Transactions'):
    st.dataframe(rep.top_transactions(df), use_container_width=True)
with st.expander('Monthly Breakdown by Category'):
    st.dataframe(rep.monthly_summary(df), use_container_width=True)
with st.expander('Full Raw Data'):
    st.dataframe(df, use_container_width=True)
