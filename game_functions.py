import sys
import pygame
from random import randint
from herbivore import Herbivore
from player import Player
def check_keydown_events(event, player): #Add (ai_settings, screen) if handling more than movement
#Respond to keypresses.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        player.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.moving_down = True

def check_keyup_events(event, player):
#Respond to key releases.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        player.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.moving_down = False

def check_events(ai_settings, screen, player):
#Respond to keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def update_screen(ai_settings, screen, all_sprites):
#Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)  
    sorted_sprites = sorted(all_sprites, key=lambda sprite: sprite.hitbox.bottom)
    # Blit sprites that move in order based on pos.y
    for sprite in sorted_sprites:
        screen.blit(sprite.image, sprite.rect)
   
    #Rect debugging
    #pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
    #for sprite in all_sprites:
        #pygame.draw.rect(screen, (255, 0, 0), herb.hitbox, 2)
    
# Make the most recently drawn screen visible.
    pygame.display.flip()

def crits_update(player, all_herbs, dt):
        player.update(all_herbs, dt)
        all_herbs.update(dt)   # Runs the update() method on every NPC in the group

def generate_herbs(ai_settings, screen, player, num, *groups):
        for i in range(num):
            x =randint(20,ai_settings.screen_width)
            y =randint(20,ai_settings.screen_height)
            herb = Herbivore(ai_settings, screen, player, groups[0], x, y)
            groups[0].add(herb)
            groups[1].add(herb)