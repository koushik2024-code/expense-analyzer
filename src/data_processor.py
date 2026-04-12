import pandas as pd

class DataProcessor:

    def load(self, filepath):
        df = pd.read_csv(filepath)
        return self.clean(df)

    def clean(self, df):
        df.columns = df.columns.str.strip().str.lower()
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df.dropna(subset=['amount', 'description', 'date'], inplace=True)
        df['description'] = df['description'].str.strip().str.lower()
        df['month'] = df['date'].dt.to_period('M').astype(str)
        df['day_of_week'] = df['date'].dt.day_name()
        df['week'] = df['date'].dt.isocalendar().week.astype(int)
        return df.reset_index(drop=True)
