
import pygame
from random import randint
from planter import Planter
from herbivore import Herbivore
from player import Player
from static_object import Static_object
from score_board import ScoreBoard
from ui import Button

def init_buttons(screen):
    ui_elements = {
        "start_menu": {
            "play_button": Button(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50, "PLAY"),
            "load_button": Button(screen.get_width() // 2 - 300, screen.get_height() // 2 + 50, 200, 50, "LOAD GAME")
        },
        "load_menu": {
            "load_1": Button(screen.get_width() // 2 - 300, screen.get_height() // 2 + 50, 200, 50, "LOAD SAVED GAME")
            },
        "playing": {
            "save_button": Button(screen.get_width() - 120, 20, 100, 40, "SAVE")
        }
    }
    return ui_elements

def generate_herbs(ai_settings, screen, player, num, score, *groups):
        for i in range(num):
            x =randint(20,ai_settings.screen_width)
            y =randint(20,ai_settings.screen_height)
            herb = Herbivore(screen, player, x, y, score, *groups)
            groups[0].add(herb)
            groups[1].add(herb)

def generate_walls(ai_settings, screen, group):
    scr_w = ai_settings.screen_width
    scr_h = ai_settings.screen_height
    wall_w = [106, scr_w+200, scr_w+200, 106]
    wall_h = [scr_w, 106, 106, scr_w]
    x_coord = [-97, 0, 0, scr_w-3]
    y_coord = [0, -50, scr_h-6, 0]
    for i in range(4):
        wall = Static_object(screen, x = x_coord[i], y = y_coord[i], width = wall_w[i], height = wall_h[i])
        group.add(wall)

def generate_planters(ai_settings, screen, player, *groups):
        num = 4
        x_coord = [576,640]
        y_coord = [352,416]
        for i in range(num):
            x = x_coord[i%2]
            y = y_coord[i//2]
            planter = Planter(screen, x, y, *groups)
            groups[0].add(planter)

def generate_assets(ai_settings, screen):
    all_herbs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    all_plants = pygame.sprite.Group()
    #Player character
    score = ScoreBoard(screen, ai_settings.screen_width)
    player = Player(screen, 600, 350, score,all_herbs, all_plants)
    all_sprites.add(player)
    #NPCs
    generate_herbs(ai_settings, screen, player, 10, score, all_herbs, all_sprites, all_obstacles, all_plants)
    #Outer boundaries
    generate_walls(ai_settings, screen, all_obstacles)
    #Planters
    generate_planters(ai_settings, screen, player, all_plants)

    return player, all_sprites, all_plants, score

def load_assets(ai_settings, screen, saved_file):
    all_herbs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    all_plants = pygame.sprite.Group()
    score = ScoreBoard(screen, ai_settings.screen_width, **saved_file["stats"])
    player = Player(screen, 600, 350, score,all_herbs, all_plants)
    player_data = saved_file["player"]
    player.pos = pygame.math.Vector2(player_data.get("x"), player_data.get("y"))
    player.vel = pygame.math.Vector2(player_data.get("vel_x"), player_data.get("vel_y"))
    all_sprites.add(player)
    herb_data = saved_file["bunnies"]
    groups =  all_herbs, all_sprites, all_obstacles, all_plants
    for data in herb_data:
        herb = Herbivore(screen, player, data.get("x"), data.get("y"), score, *groups)
        herb.vel = pygame.math.Vector2(data.get("vel_x"), data.get("vel_y"))   
        herb.state = data.get("state")
        groups[0].add(herb)
        groups[1].add(herb)  
    generate_walls(ai_settings, screen, all_obstacles)
    plant_data = saved_file["planters"]
    for data in plant_data:
        planter = Planter(screen, data.get("x"), data.get("y"), all_plants)
        planter.state = data.get("state")
        all_plants.add(planter)
        
    return player, all_sprites, all_plants, score