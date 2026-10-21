from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

client = MongoClient("mongodb://localhost:27017")
db = client.Bunnies
app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hello World!"}

@app.post("/save")
def save_game(data: StatsData):
    # 1. Catch the simple Python data from Pygame
    coins_to_save = data.coins 
    
    # 2. Translate it into the specific language MongoDB requires
    # Pygame has no idea what "insert_one" means, but server.py does!
    db.saves.insert_one({"coins": coins_to_save}) 
    
    return {"message": "Translation and save successful!"}