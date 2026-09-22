import pygame

class Creature():
    def __init__(self, ai_settings, screen):
        crit_image = pygame.image.load('graphics/carn.png')
        new_width = 60
        new_height = int(crit_image.get_height() * (new_width / crit_image.get_width())) 
        #Initialize the scrit and set its starting position.
        self.screen = screen 
        self.ai_settings = ai_settings 
        # Load the crit image and get its rect.
        self.image = pygame.transform.scale(crit_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Start each new crit at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
#Update the crit's position based on the movement flag and current speed.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_horizontal += self.ai_settings.crit_speed
        if self.moving_left and self.rect.left > 0:
            self.center_horizontal -= self.ai_settings.crit_speed
        if self.moving_up and self.rect.top > 0:
            self.center_vertical -= self.ai_settings.crit_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_vertical += self.ai_settings.crit_speed
        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical

    def blitme(self):
 #Draw the scrit at its current location."""
        self.screen.blit(self.image, self.rect)