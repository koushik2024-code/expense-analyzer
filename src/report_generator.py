class ReportGenerator:

    def monthly_summary(self, df):
        return (
            df.groupby(['month', 'category'])['amount']
            .sum().unstack(fill_value=0).round(2)
        )

    def top_transactions(self, df, n=10):
        return (
            df.nlargest(n, 'amount')[['date','description','amount','category']]
            .reset_index(drop=True)
        )

    def generate_text_summary(self, savings_info):
        lines = [
            f"Total Spent      : Rs {savings_info['total_spent']:,}",
            f"Avg Monthly Spend: Rs {savings_info['avg_monthly']:,}",
            f"Savings Rate     : {savings_info['savings_rate_%']}%",
            f"Biggest Category : {savings_info['top_category']}",
            f"Months Analyzed  : {savings_info['total_months']}",
        ]
        return '\n'.join(lines)
