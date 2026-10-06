from src.connector import fetch_transactions
# from google import genai
    

async def predict(account_id) -> dict:
    print(f"Your account_id: {account_id}")
    transactions = await fetch_transactions(account_id) or None
    
    return {
        "predicted_next_transaction": {
            "amount": 12.3,
            "category": "Food",
            "transactions": transactions             
        }
    }
