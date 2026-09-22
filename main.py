import pygame
from settings import Settings
from creature import Creature
import game_functions as gf
from pygame.sprite import Group

# Initialize game and create a screen object.
def run_game():
    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    crit = Creature(ai_settings, screen)
#Main loop
    running = True
    while running:
        gf.check_events(ai_settings, screen, crit)
        crit.update()
        gf.update_screen(ai_settings, screen, crit)

run_game()
