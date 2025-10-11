import pandas as pd
from src.connector import fetch_transactions
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# from pandas import pd

def prep_data(df: pd.DataFrame):
    df['timestamp'] = pd.to_datetime(df['date'])
    df['day'] = df['timestamp'].dt.day
    df['weekday'] = df['weekday'].dt.weekday
    df['month'] = df['month'].dt.month
    df['amount'] = df['amount'].astype(float)
    
    return df


def predict_next_amount(df):
    x = df[["day", "week", "month"]]
    y = df["amount"]
    
    
    model = LinearRegression()
    model.fit(x, y)
    
    
    next_day = pd.DataFrame({
        "month": [df['month'].max()],
        "day": [df['day'].max() + 1],
        "week": [(df["week"].max() + 1) % 7]
    })
    
    predicated_amount = model.predict(next_day)[0]
    return round(predicated_amount, 2)
    

async def predict_transactions(queries) -> dict:
    print(f"Your queries: {queries}")
    transactions = await fetch_transactions(queries) or None
    
    print(transactions)
    return {
        "predicted_next_transaction": {
            "amount": 12.3,
            "category": "Food"              
        }
    }