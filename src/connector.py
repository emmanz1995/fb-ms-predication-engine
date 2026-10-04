import os
import requests
from dotenv import load_dotenv
from typing import List

base_url = os.environ.get("BASE_URL")


async def fetch_transactions(queries) -> List[dict]:
    account_id = queries['account_id']
    
    transactions = []
    
    
    #TODO: get access token somehow 
    token = ""
    try:
        resp = await requests.get(
            url=f"{base_url}/api/v1/account/transactions?currentPage=1&limit=10&accountId={account_id}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
        total_pages = resp.json()['pagination']['totalPages']
        
        for page in range(1, total_pages + 1):
            resp = await requests.get(
                url=f"{base_url}/api/v1/account/transactions?currentPage={page}&limit=10&accountId={account_id}"
            )
            
            
            transactions.append(**resp["transactions"])
            
            
            if resp.json()["pagination"]["totalPages"] < page:
                break;
            
            
        if resp.status_code == 400:
            raise Exception('Failed to get transactions')
        
    except Exception as e:
        print(f"Error occurred here...", e)
        raise Exception('Failed with an internal server error', e)
    
    return transactions