from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.predict.predict import predict

class PredictedTransaction(BaseModel):
    price: float
    category: str

class PredictionModel(BaseModel):
    predicted_next_transaction: PredictedTransaction

class PredictionReqBody(BaseModel):
    account_id: str
    
    
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8083",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the prediction engine service"
    }

@app.post("/api/v1/predict")
async def predict_transactions(payload: PredictionReqBody):
    #TODO: get access token somehow 
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIyNzRlZGUzZS1mNzZjLTRlNjgtYmMxZC1iMDc4YjdhMTAxY2UiLCJ1c2VybmFtZSI6ImVtbWFuejk1IiwiaWF0IjoxNzkxMzIxMTE1LCJleHAiOjE3OTE0MDcxMTUsImF1ZCI6ImZiLWF1ZC1hcGkiLCJpc3MiOiJmYi1pc3MtYXV0aCJ9.TSRGRXyrZ5txHyuceRm71VLbqdiCbaXcuRVpgII5tz2LIN7QxR1cxl275OjegZQQy0pcbjsx_D7INkeXhrixDrQcoVSCZ0fHmYV0PgxgoiL1VhkRxXQ6B-pMGPESM-EOSgxyVoFp4yE8pswHzJVoSfh7lwSSQrfO1c6Ye9bUhUI1ZYvXZp_wmC_JkPW3-dfxqYDzJlmZQ2J7tVH-sQV4wP6_5EIfQhhA8A8ikOmXu4y1bzdDk2h-3WL-VQDALhFQj6X886I1Epz_ja3VmssCkdXTt4PRH5_t49jU2xBA5F5FNyl_tii53l9EtWnHLoVu8M1gvX1tUm2zNrgQf612zDLGZg7ADUJMOid6rwi6zNwe0aoJBik0lQnWXaGtQC4BHvXcJbYGVlBdrkFj2sg--Liu6KFaPg63jl6ugaMkvQV18X37QtqlqfbtyTt4JKthCgfFmPnskE_iATxY6WDuyWcC2CKnvTv8PTS6MQKhVCOMYaaoFdblXbe90rwnlOxNkTwttP5BiJ--KPLpNVERLQMA6KDCYhtAwG3zlsschO5KaWGbbWZiP7qtfAOyUD05rewujkfBAgtO9wBedHY3YqkAHYkd7a4Sxoi-3PhHjZjfesavLdW9qDc8cLwg9mN2hBwl3EbqEYHjgIYMnMfT13iiCMGTgTXLZT7wzxX6mF0"
    account_id = payload.account_id
    predicted_transactions = await predict(account_id, token)
    return {"response": predicted_transactions}

def main() -> None:
    print("Main starting point")


if __name__ == "__main__":
    app.setup()