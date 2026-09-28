from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, player, all_herbs, x, y):
        # Pass herbivore-specific attributes to Creature
        stats = {
            "sprite_sheet": 'graphics/slime.png',
            "animation_steps": [6, 6, 6, 6],
            "animation_rows": [3, 4, 4, 5],
            "frame_size_x": 32,
            "frame_size_y": 32,
            "height": 64,
            "width": 64,
            "energy": 100,
            "speed": random.uniform(0,0.15),
            "inflate_rect": [-40,-40],
            "herbs": all_herbs,
            "player": player
            }
        super().__init__(ai_settings, screen, **stats, x=x, y=y)
        

        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        

    def update(self): 
        current_time = pygame.time.get_ticks() 
        if self.escaping and current_time - self.updated >= self.interval:
                self.vel.scale_to_length(self.speed)
                self.escaping = False

        # Check X boundaries (Left and Right)
        if self.hitbox.left <= 0 or self.hitbox.right >= self.ai_settings.screen_width:
            self.vel.x *= -1  # Reverses horizontal direction instantly 
        # Check Y boundaries (Top and Bottom)
        if self.hitbox.top <= 0 or self.hitbox.bottom >= self.ai_settings.screen_height:
            self.vel.y *= -1  # Reverses vertical direction instantly
        if self.vel.x == 0 or self.vel.y == 0:
            self.update_velocity()
        self.player_collision()
        self.check_collisions(self.herbs)
        self.update_flag()
            #Update position based on movement flags and speed.
        
        self.pos += self.vel
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
        self.animate(current_time) 
        self.rect.center = self.hitbox.center
        # Sync integer screen rect with precise float tracking
