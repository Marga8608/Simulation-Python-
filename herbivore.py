from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, all_herbs, x, y):
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
            "speed": random.uniform(0,0.3)
            }
        super().__init__(ai_settings, screen, **stats, x=x, y=y)
        

        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        self.interval = random.randint(1500, 4000)

    def update(self): 
        current_time = pygame.time.get_ticks()   
        self.animate(current_time)  
        '''if current_time - self.updated >= self.interval:
            self.update_velocity()
            self.updated = current_time
            self.interval = random.randint(1500, 10000)
            self.speed = random.uniform(0,0.3) '''
        # Check X boundaries (Left and Right)
        if self.rect.left <= 0 or self.rect.right >= self.ai_settings.screen_width:
            self.vel.x *= -1  # Reverses horizontal direction instantly 
        # Check Y boundaries (Top and Bottom)
        if self.rect.top <= 0 or self.rect.bottom >= self.ai_settings.screen_height:
            self.vel.y *= -1  # Reverses vertical direction instantly
        if self.vel.x == 0 or self.vel.y == 0:
            self.update_velocity()
        self.update_flag()
            #Update position based on movement flags and speed.
        self.pos += self.vel

        # Sync integer screen rect with precise float tracking
        self.rect.center = (round(self.pos.x), round(self.pos.y))