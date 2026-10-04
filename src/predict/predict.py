from src.connector import fetch_transactions
# from google import genai
    

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
