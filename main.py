import pygame
from random import randint
from settings import Settings
from player import Player
import game_functions as gf
from pygame.sprite import Group

# Initialize game and create a screen object.
def run_game():
    
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    clock = pygame.time.Clock()

    #Groups
    all_sprites = pygame.sprite.Group()
    all_herbs = pygame.sprite.Group() 
    all_static = pygame.sprite.Group()
    #Player character
    player = Player(ai_settings, screen, 600, 350)
    all_sprites.add(player)
    #NPCs
    gf.generate_herbs(ai_settings, screen, player, 10, all_herbs, all_sprites)
    #Outer boundaries


    #Main loop
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        gf.check_events(ai_settings, screen, player)
        gf.crits_update(player, all_herbs, dt)
        gf.update_screen(ai_settings, screen, all_sprites)

run_game()
