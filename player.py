from creature import Creature
import pygame

class Player(Creature):
    def __init__(self, ai_settings, screen, x=None, y=None):
        # Pass herbivore-specific image and coordinates to base Creature
        super().__init__(ai_settings, screen, x=x, y=y)
        
        # Player-specific attributes
        #crit_image = pygame.image.load(ai_settings.herb_image)
        #self.image = pygame.transform.scale(crit_image, (self.width, self.height))
        self.speed = 1 #Overwrites the speed of Creature
        self.energy = 100


            # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #Update position based on movement flags and speed.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.pos.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.pos.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.pos.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.pos.y += self.speed
        # Sync integer screen rect with precise float tracking
        self.rect.center = (round(self.pos.x), round(self.pos.y))