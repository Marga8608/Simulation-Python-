import sys
import pygame

def check_keydown_events(event, ai_settings, screen, crit):
#Respond to keypresses.
    if event.key == pygame.K_RIGHT:
        crit.moving_right = True
    elif event.key == pygame.K_LEFT:
        crit.moving_left = True
    elif event.key == pygame.K_UP:
        crit.moving_up = True
    elif event.key == pygame.K_DOWN:
        crit.moving_down = True

def check_keyup_events(event, crit):
#Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        crit.moving_right = False
    elif event.key == pygame.K_LEFT:
        crit.moving_left = False
    elif event.key == pygame.K_UP:
        crit.moving_up = False
    elif event.key == pygame.K_DOWN:
        crit.moving_down = False

def check_events(ai_settings, screen, crit):
#Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, crit)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, crit)

def update_screen(ai_settings, screen, crit, herbs):
#Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)  
    crit.blitme()
    herbs.draw(screen)
# Make the most recently drawn screen visible.
    pygame.display.flip()

def crits_update(player, all_herbs):
        player.update()
        #for herb in all_herbs:
            #herb.update_velocity()
        all_herbs.update()   # Runs the update() method on every NPC in the group
