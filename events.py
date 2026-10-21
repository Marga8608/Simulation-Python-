import pygame

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

def check_mouse_events(buttons, current_state):
    mouse_pos = pygame.mouse.get_pos()
    if current_state == "start_menu":
        if buttons["play_button"].is_clicked(mouse_pos):
            return("playing")
    elif current_state == "PLAYING":
        if buttons["save_button"].is_clicked(mouse_pos):
            # API save logic 
            return current_state

def check_events(player, buttons, current_state):
#Respond to keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, current_state
        else:
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event, player)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_state = check_mouse_events(buttons, current_state)
    return True, current_state
                
    
