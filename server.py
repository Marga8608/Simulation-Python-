from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

client = MongoClient("mongodb://localhost:27017")
db = client.Bunnies
app = FastAPI()

class StatsData(BaseModel):
    coins: int
    carrots_eaten: int
    carrots_saved: int
    carrots_picked: int

class PlayerData(BaseModel):
    x : int
    y : int
    vel_x : int
    vel_y :int
    

class BunnyData(BaseModel):
    x: int
    y: int
    vel_x : int
    vel_y :int

class PlanterData(BaseModel):
    x: int
    y: int
    state : str

class SavedData(BaseModel):
    stats: StatsData
    player: PlayerData
    bunnies: List[BunnyData]
    planters: List[PlanterData]

@app.get("/")
def home():
    return {"message" : "Hello World!"}

@app.post("/save")
def save_game(data: SavedData):
    # 1. Catch the simple Python data from Pygame
    save_file_query = {"save_slot": "slot_1"}
    new_data = {"$set": data.model_dump()}
    # 2. Translate it into the specific language MongoDB requires
    # Pygame has no idea what "insert_one" means, but server.py does!
    db.saves.update_one(save_file_query, new_data, upsert=True)   
    return {"message": "Translation and save successful!"}