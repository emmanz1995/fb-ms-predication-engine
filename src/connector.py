import os
import requests
import httpx
from dotenv import load_dotenv
from typing import List

load_dotenv()
base_url = os.environ.get("BASE_URL")

async def fetch_transactions(account_id) -> List[dict]:
    transactions: List[dict] = []
    
    #TODO: get access token somehow 
    token = ""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                url=f"{base_url}/api/v1/transactions?currentPage=1&limit=10&accountId={account_id}",
                headers={
                    "Authorization": f"Bearer {token}"
                }
            )
            
            if resp.status_code == 400:
              raise Exception('Failed to get transactions')
        
        total_pages = resp.json()['pagination']['totalPages']
        
        for page in range(1, total_pages + 1):
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    url=f"{base_url}/api/v1/transactions?currentPage={page}&limit=10&accountId={account_id}",
                     headers={
                        "Authorization": f"Bearer {token}"
                    }
                )
            
                resp.raise_for_status()
                data = resp.json()
                
                transactions_page = data["transactions"]
                transactions.extend(transactions_page)
                
                
                if resp.json()["pagination"]["totalPages"] < page:
                    break;
                
    except httpx.HTTPError:
        print("HTTP error:", e) 
        raise Exception("Failed to fetch transactions") from e
        
    except Exception as e:
        print(f"Error occurred here...", e)
        raise Exception('Failed with an internal server error', e)
    
    return transactions