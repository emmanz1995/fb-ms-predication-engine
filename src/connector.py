import os
import requests
from dotenv import load_dotenv

base_url = os.environ.get("BASE_URL")


async def fetch_transactions(queries) -> dict:
    account_id = queries['account_id']
    limit = queries['limit']
    current_page = queries['current_page']
    
    print(account_id)
    print(limit)
    print(current_page)
    
    try:
        resp = await requests.get(
            url=f"{base_url}/api/v1/account/transactions"
        )
        
        
        if resp.status_code == 400:
            raise Exception('Failed to get transactions')
        
        return resp.json()
    except Exception as e: 
        print(f"Error occurred here...", e)