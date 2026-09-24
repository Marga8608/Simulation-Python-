import pygame
import random

class Creature(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, x=None, y=None):
        # 1. Initialize Pygame's Sprite parent class
        super().__init__()
        
        self.screen = screen 
        self.ai_settings = ai_settings 
        self.screen_rect = self.screen.get_rect()
        self.speed = self.ai_settings.crit_speed
        

        # 2. Load and scale image
        crit_image = pygame.image.load(ai_settings.crit_image)
        self.width = 60
        self.height = int(crit_image.get_height() * (self.width / crit_image.get_width())) 
        self.image = pygame.transform.scale(crit_image, (self.width, self.height))
        self.rect = self.image.get_rect()

        # 3. Position setup (default to screen center if x, y are not provided)
        start_x = x if x is not None else self.screen_rect.centerx
        start_y = y if y is not None else self.screen_rect.centery
        self.pos = pygame.math.Vector2(start_x, start_y)
        self.rect.center = (round(self.pos.x), round(self.pos.y))



    def blitme(self):
        #Draw the creature manually (if not using Pygame Group drawing).
        self.screen.blit(self.image, self.rect)

    def update_velocity(self):
            self.angle = random.uniform(0,360)
            self.vel.from_polar((self.speed, self.angle))
    
    def update_flag(self):
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
            
    
    