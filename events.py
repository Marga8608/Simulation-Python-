import pygame
import api


def check_keydown_events(event, player): #Add (ai_settings, screen) if handling more than movement
#Respond to keypresses.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        player.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.moving_down = True
    if event.key == pygame.K_e:
            player.plot_interact()

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

def check_mouse_events(buttons, current_state, to_save):
    mouse_pos = pygame.mouse.get_pos()
    if current_state == "start_menu":
        if buttons["play_button"].is_clicked(mouse_pos):
            return("playing")
        if buttons["load_button"].is_clicked(mouse_pos):
            return("load_menu") 
    elif current_state == "load_menu":
        if buttons["load_1"].is_clicked(mouse_pos):
            return("loading")
    elif current_state == "PLAYING":
        if buttons["save_button"].is_clicked(mouse_pos):
            api.save_game(*to_save)
            return current_state

def check_events(to_save, buttons, current_state):
#Respond to keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, current_state
        else:
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event, to_save[0])
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, to_save[0])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_state = check_mouse_events(buttons, current_state, to_save)
    return True, current_state
                
    
