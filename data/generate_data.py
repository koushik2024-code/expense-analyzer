import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

descriptions = {
    "Food":          ["Swiggy order", "Zomato pizza", "Big Bazaar groceries", "Cafe Coffee Day", "Dominos"],
    "Travel":        ["Ola cab", "Uber ride", "IndiGo flight", "IRCTC train ticket", "Metro card recharge"],
    "Shopping":      ["Amazon purchase", "Flipkart order", "Myntra clothes", "Reliance Digital", "D-Mart"],
    "Entertainment": ["Netflix subscription", "BookMyShow movie", "Spotify premium", "Steam game", "YouTube Premium"],
    "Utilities":     ["Electricity bill", "Airtel recharge", "Water bill", "LPG gas cylinder", "Broadband bill"],
    "Health":        ["Apollo pharmacy", "Gym membership", "Doctor consultation", "MedPlus medicines"],
}

rows = []
start = datetime(2024, 1, 1)
for i in range(500):
    category = random.choice(list(descriptions.keys()))
    desc = random.choice(descriptions[category])
    amount = round(random.uniform(50, 5000), 2)
    date = start + timedelta(days=random.randint(0, 365))
    rows.append({"date": date.strftime("%Y-%m-%d"), "description": desc, "amount": amount, "category": category})

df = pd.DataFrame(rows)
df.to_csv("data/sample_data.csv", index=False)
print("Generated 500 transactions.")