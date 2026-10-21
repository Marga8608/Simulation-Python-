import pygame

def update_screen(screen, bg, score, all_sprites, all_plants):
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