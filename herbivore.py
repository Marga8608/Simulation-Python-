from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, all_herbs, x, y):
        # Pass herbivore-specific image and coordinates to base Creature
        super().__init__(ai_settings, screen, x=x, y=y)
        
        # Herbivore-specific attributes
        crit_image = pygame.image.load(ai_settings.herb_image)
        self.image = pygame.transform.scale(crit_image, (self.width, self.height))
        self.energy = 100
        self.herb_group = all_herbs
        self.speed = random.uniform(0,0.5)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.angle = random.uniform(0,360)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        self.interval = random.randint(1500, 4000)

    def update(self): 
            #Random direction changes
        current_time = pygame.time.get_ticks()
        if current_time - self.updated >= self.interval:
            self.update_velocity()
            self.updated = current_time
            self.interval = random.randint(1500, 10000)
            self.speed = random.uniform(0,0.3)
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
        if self.moving_right:
            self.pos.x += self.vel.x
        if self.moving_left:
            self.pos.x += self.vel.x
        if self.moving_up:
            self.pos.y += self.vel.y
        if self.moving_down:
            self.pos.y += self.vel.y
        # Sync integer screen rect with precise float tracking
        self.rect.center = (round(self.pos.x), round(self.pos.y))