import sys
import pygame
from random import randint
from planter import Planter
from herbivore import Herbivore
from player import Player
from static_object import Static_object
from score_board import ScoreBoard

#Event checkers
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

def check_events(ai_settings, screen, player):
#Respond to keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
            
#Updaters
def update_screen(ai_settings, screen, bg, score, all_sprites, all_plants):
#Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
    screen.blit(bg) 
    all_plants.draw(screen) 
    score.draw()
    sorted_sprites = sorted(all_sprites, key=lambda sprite: sprite.hitbox.bottom)
    # Blit sprites that move in order based on pos.y
    for sprite in sorted_sprites:
        screen.blit(sprite.image, sprite.rect)
   
    #Rect debugging
    #pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
    #for sprite in all_sprites:
        #pygame.draw.rect(screen, (255, 0, 0), herb.hitbox, 2)
    pygame.display.flip()

def sprites_update(all_sprites, all_plants, dt):
        all_plants.update(dt)
        all_sprites.update(dt)   # Runs the update() method on every NPC in the group
#Generators
def generate_herbs(ai_settings, screen, player, num, score, *groups):
        for i in range(num):
            x =randint(20,ai_settings.screen_width)
            y =randint(20,ai_settings.screen_height)
            herb = Herbivore(ai_settings, screen, player, x, y, score, *groups)
            groups[0].add(herb)
            groups[1].add(herb)

def generate_walls(ai_settings, screen, group):
    scr_w = ai_settings.screen_width
    scr_h = ai_settings.screen_height
    wall_w = [100, scr_w+200, scr_w+200, 100]
    wall_h = [scr_w, 100, 100, scr_w]
    x_coord = [-100, 0, 0, scr_w]
    y_coord = [0, -50, scr_h, 0]
    for i in range(4):
        wall = Static_object(ai_settings, screen, x = x_coord[i], y = y_coord[i], width = wall_w[i], height = wall_h[i])
        group.add(wall)

def generate_planters(ai_settings, screen, player, *groups):
        num = 4
        x_coord = [608,640]
        y_coord = [384,416]
        for i in range(num):
            x = x_coord[i%2]
            y = y_coord[i//2]
            planter = Planter(ai_settings, screen, x, y, *groups)
            groups[0].add(planter)

def generate_assets(ai_settings):
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    background = pygame.image.load(ai_settings.background).convert()
#Groups
    all_herbs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    all_plants = pygame.sprite.Group()
    #Player character
    score = ScoreBoard(screen)
    player = Player(ai_settings, screen, 600, 350, score,all_herbs, all_plants)
    all_sprites.add(player)
    #NPCs
    generate_herbs(ai_settings, screen, player, 10, score, all_herbs, all_sprites, all_obstacles, all_plants)
    #Outer boundaries
    generate_walls(ai_settings, screen, all_obstacles)
    #Planters
    generate_planters(ai_settings, screen, player, all_plants)

    return screen, player, background, all_sprites, all_plants, score