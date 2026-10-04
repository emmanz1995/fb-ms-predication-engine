from fastapi import FastAPI
from pydantic import BaseModel
from src.predict.predict import predict_transactions

class PredictedTransaction(BaseModel):
    price: float
    category: str

class PredictionModel(BaseModel):
    predicted_next_transaction: PredictedTransaction

class PredictionReqBody(BaseModel):
    account_id: str
    
    
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the prediction engine service"
    }

@app.post("/api/v1/predict")
async def predict_transactions(body: PredictionReqBody):
    account_id = body.account_id
    
    predicted_transactions = await predict_transactions({"account_id": account_id})
    return {"response": predicted_transactions}

def main() -> None:
    print("Main starting point")


if __name__ == "__main__":
    app.setup()