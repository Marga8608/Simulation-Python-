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

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 1
        self.angle = random.uniform(0,360)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.speed, self.angle))

    def update_velocity(self):
        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        if self.vel.x > 0:
            self.moving_right = True
            self.moving_left = False
        if self.vel.x < 0:
            self.moving_left = True
            self.moving_right = False
        if self.vel.y > 0:
            self.moving_down = True
            self.moving_up = False
        if self.vel.y < 0:
            self.moving_up = True
            self.moving_down = False
        

    def update(self):

        #Update position based on movement flags and speed.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.pos.x += self.vel.x
        if self.moving_left and self.rect.left > 0:
            self.pos.x += self.vel.x
        if self.moving_up and self.rect.top > 0:
            self.pos.y += self.vel.y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.pos.y += self.vel.y
        # Sync integer screen rect with precise float tracking
        self.rect.center = (round(self.pos.x), round(self.pos.y))