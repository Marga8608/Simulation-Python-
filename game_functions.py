import sys
import pygame

def check_keydown_events(event, player): #Add (ai_settings, screen) if handling more than movement
#Respond to keypresses.
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True

def check_keyup_events(event, player):
#Respond to key releases.
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
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

def update_screen(ai_settings, screen, player, herbs):
#Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)  
    player.blitme()
    pygame.draw.rect(screen, (255, 0, 0), player.rect, 2)
    herbs.draw(screen)
# Make the most recently drawn screen visible.
    pygame.display.flip()

def crits_update(player, all_herbs):
        player.update()
        all_herbs.update()   # Runs the update() method on every NPC in the group

