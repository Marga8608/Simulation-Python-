import pygame
import sys
import subprocess
from random import randint
from settings import Settings
import game_functions as gf
import events
import ui
import render


# Initialize game and create a screen object.
def run_game():
    # Start the FastAPI server in the background
    print("Starting server...")
    server_process = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "server:app", "--port", "8000"],
    stdout=subprocess.DEVNULL, # Hides the server's terminal spam so it doesn't clutter Pygame's prints
    stderr=subprocess.DEVNULL
)
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    background = pygame.image.load(ai_settings.background).convert()
    player, all_sprites, all_plants, score = gf.generate_assets(ai_settings, screen)
    
    ui_elements = gf.init_buttons(screen)
    current_state = "start_menu"
    running = True
   
    while running:
        dt = clock.tick(60) / 1000.0
        running, current_state = events.check_events(player, ui_elements.get(current_state), current_state)
        if current_state == "start_menu":
            ui.start(screen, ui_elements.get(current_state)) 
        elif current_state == "playing":
            has_active_crops = any(not plant.state == "empty" for plant in all_plants)
            if score.coins <= 0 and not has_active_crops: 
                current_state = "game_over"
                continue   
            render.sprites_update(all_sprites, all_plants, dt)
            render.update_screen(screen, background, score, all_sprites, all_plants) 
        elif current_state == "game_over":
            ui.game_over(screen)

    print("Saving to database and shutting down the server...")
    pygame.quit()
    # Terminate the background server process so it doesn't run forever
    server_process.terminate()
    sys.exit()
run_game()
