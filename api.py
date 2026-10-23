import requests

BASE_URL = "http://localhost:8000"

def save_game(player, bunny_list, planter_list, score):
    """Packs the active game state and sends it to the server."""
    
    # 1. Structure the data exactly as your Pydantic SaveData model expects
    data = {
        # player.to_dict() MUST return x, y, vel_x, and vel_y floats
        "player": player.to_dict(),  
        # These lists contain the individual bunny and planter dictionaries
        "bunnies": [bunny.to_dict() for bunny in bunny_list],
        "planters": [planter.to_dict() for planter in planter_list],
        "stats": {
            "coins": score.coins,
            "carrots_eaten": score.carrots_eaten,
            "carrots_saved": score.carrots_saved,
            "carrots_picked": score.carrots_picked
        }
    }

    try:
        response = requests.post(f"{BASE_URL}/save", json=data)
        response.raise_for_status() # Triggers an error if the server crashes
        print("Network: Save successful.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not save the game. {e}")
        return None

def load_game():   
    try:
        response = requests.get(f"{BASE_URL}/load")
        response.raise_for_status()
        
        saved_data = response.json()
        
        # If MongoDB returned nothing (brand new player), this will be None
        if saved_data is None:
            print("Network: No save file found.")
            return None
            
        print("Network: Save file downloaded successfully.")
        return saved_data
        
    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not load the game. {e}")
        return None