import pandas as pd

class Predictor:

    def monthly_trend(self, df):
        return df.groupby('month')['amount'].sum().reset_index()

    def category_split(self, df):
        return df.groupby('category')['amount'].sum().reset_index()

    def weekly_trend(self, df):
        return df.groupby('week')['amount'].sum().reset_index()

    def daywise_trend(self, df):
        order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        result = df.groupby('day_of_week')['amount'].sum().reindex(order).reset_index()
        return result

    def savings_analysis(self, df, income=50000):
        total_spent  = df['amount'].sum()
        months       = df['month'].nunique()
        avg_monthly  = total_spent / months if months > 0 else total_spent
        savings_rate = max(0, (income - avg_monthly) / income * 100)
        top_category = df.groupby('category')['amount'].sum().idxmax()
        return {
            'total_spent':    round(total_spent, 2),
            'avg_monthly':    round(avg_monthly, 2),
            'savings_rate_%': round(savings_rate, 1),
            'top_category':   top_category,
            'total_months':   months,
        }

    def budget_recommendations(self, df):
        cat_totals = df.groupby('category')['amount'].sum()
        total      = cat_totals.sum()
        tips       = []
        for cat, amt in cat_totals.items():
            pct = amt / total * 100
            if pct > 35:
                tips.append(f'Warning: {cat} is {pct:.1f}% of your budget - try to reduce it.')
            elif pct > 25:
                tips.append(f'Note: {cat} is {pct:.1f}% of spending - keep an eye on it.')
        if not tips:
            tips.append('Your spending is well balanced across categories!')
        return tips
