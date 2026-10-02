import pygame
from random import randint
from settings import Settings
import game_functions as gf


# Initialize game and create a screen object.
def run_game():
    
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    screen, player, background, all_sprites, all_plants, score = gf.generate_assets(ai_settings)

    #Main loop
    running = True
    game_active = True
    in_start_screen = True
    

    button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)
    game_over_font = pygame.font.Font(None, 74)

    while running:
        dt = clock.tick(60) / 1000.0
        in_start_screen = gf.check_events(ai_settings, screen, player, button_rect, in_start_screen)
        if in_start_screen:
            gf.start(screen, button_rect) 
        else:
            has_active_crops = any(not plant.empty for plant in all_plants)
            if score.coins <= 0 and not has_active_crops: 
                game_active = False
        
            if game_active:
                gf.sprites_update(all_sprites, all_plants, dt)
                gf.update_screen(ai_settings, screen, background, score, all_sprites, all_plants)
        
            else:
                screen.fill("black")
                text_surface = game_over_font.render("You Are Out of Coins!", True, "red")
                screen.blit(text_surface, (screen.get_width() // 2 - 150, screen.get_height() // 2 - 50))
                pygame.display.flip()
run_game()
