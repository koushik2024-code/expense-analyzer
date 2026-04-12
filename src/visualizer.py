import plotly.express as px

class Visualizer:

    def monthly_bar(self, trend_df):
        return px.bar(trend_df, x='month', y='amount',
                      title='Monthly Total Spending',
                      labels={'amount': 'Amount (Rs)', 'month': 'Month'},
                      color_discrete_sequence=['#636EFA'])

    def category_pie(self, cat_df):
        return px.pie(cat_df, names='category', values='amount',
                      title='Spending by Category', hole=0.4)

    def category_bar(self, cat_df):
        return px.bar(cat_df.sort_values('amount'),
                      x='amount', y='category', orientation='h',
                      title='Category-wise Expenditure',
                      labels={'amount': 'Amount (Rs)', 'category': 'Category'},
                      color='amount', color_continuous_scale='Blues')

    def daily_line(self, df):
        daily = df.groupby('date')['amount'].sum().reset_index()
        return px.line(daily, x='date', y='amount',
                       title='Daily Spending Over Time',
                       labels={'amount': 'Amount (Rs)', 'date': 'Date'})

    def daywise_bar(self, daywise_df):
        return px.bar(daywise_df, x='day_of_week', y='amount',
                      title='Spending by Day of Week',
                      labels={'amount': 'Amount (Rs)', 'day_of_week': 'Day'},
                      color_discrete_sequence=['#EF553B'])
