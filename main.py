import pygame
from random import randint
from settings import Settings
import game_functions as gf


# Initialize game and create a screen object.
def run_game():
    
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    screen, player, background, all_sprites, all_plants, score = gf.generate_assets(ai_settings)

    #Main loop
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        gf.check_events(ai_settings, screen, player)
        gf.sprites_update(all_sprites, all_plants, dt)
        gf.update_screen(ai_settings, screen, background, score, all_sprites, all_plants)

run_game()
