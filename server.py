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
    x: float
    y: float
    vel_x : float
    vel_y :float
    

class BunnyData(BaseModel):
    x: float
    y: float
    vel_x : float
    vel_y :float
    state : str

class PlanterData(BaseModel):
    x: float
    y: float
    state : str

class SavedData(BaseModel):
    player: PlayerData
    bunnies: List[BunnyData]
    planters: List[PlanterData]
    stats: StatsData

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

@app.get("/load")
def load_game():
    # Find the specific save slot. 
    # {"_id": 0} tells MongoDB to strip out its internal tracking ID, 
    # because FastAPI doesn't know how to convert that specific ID into JSON.
    save_file = db.saves.find_one({"save_slot": "slot_1"}, {"_id": 0})
    
    return save_file