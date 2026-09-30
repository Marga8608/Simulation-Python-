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
    background = pygame.image.load(ai_settings.background).convert()
    clock = pygame.time.Clock()

    #Groups
    #0 = all_herbs, 1= all_sprites, 2= all_static_objects
    groups = [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
    #Player character
    player = Player(ai_settings, screen, 600, 350)
    groups[1].add(player)
    #NPCs
    gf.generate_herbs(ai_settings, screen, player, 10, *groups)
    #Outer boundaries
    gf.generate_walls(ai_settings, screen, groups[2])

    #Main loop
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        gf.check_events(ai_settings, screen, player)
        gf.crits_update(player, groups[0], dt)
        gf.update_screen(ai_settings, screen, background, groups[1])

run_game()
