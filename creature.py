import pygame

class Creature(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, image_path='graphics/carn.png', x=None, y=None):
        # 1. Initialize Pygame's Sprite parent class
        super().__init__()
        
        self.screen = screen 
        self.ai_settings = ai_settings 
        self.screen_rect = self.screen.get_rect()

        # 2. Load and scale image
        crit_image = pygame.image.load(image_path)
        new_width = 60
        new_height = int(crit_image.get_height() * (new_width / crit_image.get_width())) 
        self.image = pygame.transform.scale(crit_image, (new_width, new_height))
        self.rect = self.image.get_rect()

        # 3. Position setup (default to screen center if x, y are not provided)
        self.x = float(x if x is not None else self.screen_rect.centerx)
        self.y = float(y if y is not None else self.screen_rect.centery)
        self.rect.centerx = self.x
        self.rect.centery = self.y

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position based on movement flags and speed."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.crit_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.crit_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.crit_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.crit_speed

        # Sync integer screen rect with precise float tracking
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def blitme(self):
        """Draw the creature manually (if not using Pygame Group drawing)."""
        self.screen.blit(self.image, self.rect)