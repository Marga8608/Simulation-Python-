import pygame

class Static_object(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, image = None, **stats):
        # 1. Initialize Pygame's Sprite parent class
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        width = stats.get("width")
        height = stats.get("height")
        self.pos = pygame.math.Vector2(stats.get("x"), stats.get("y"))
        if image is not None:
            self.image = image
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(self.pos.x, self.pos.y, width, height)
        self.hitbox = self.rect.copy()
