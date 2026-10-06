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
    account_id = payload.account_id
    predicted_transactions = await predict(account_id)
    return {"response": predicted_transactions}

def main() -> None:
    print("Main starting point")


if __name__ == "__main__":
    app.setup()