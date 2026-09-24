import pygame
from random import randint
from settings import Settings
from creature import Creature
from herbivore import Herbivore
from player import Player
import game_functions as gf
from pygame.sprite import Group

# Initialize game and create a screen object.
def run_game():
    
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    #NPC groups
    all_herbs = pygame.sprite.Group()


    player = Player(ai_settings, screen)
    
    # NPCs
    for i in range(5):
        herb = Herbivore(ai_settings, screen, all_herbs, x=randint(20,ai_settings.screen_width), y=randint(20,ai_settings.screen_height))
        all_herbs.add(herb)

    #Main loop
    running = True
    while running:
        gf.check_events(ai_settings, screen, player)
        gf.crits_update(player, all_herbs)
        gf.update_screen(ai_settings, screen, player, all_herbs)

run_game()
