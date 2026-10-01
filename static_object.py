import pygame

class Static_object(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, image = None, **stats):
        # 1. Initialize Pygame's Sprite parent class
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.width = stats.get("width")
        self.height = stats.get("height")
        x = stats.get("x")
        y = stats.get("y")
        self.infl_rect = stats.get("inflate_rect", [0, 0])
        self.pos = pygame.math.Vector2(x, y)
        if image is not None:
            first_image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(first_image, (self.width, self.height))  
            self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        else:
            self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.hitbox = self.rect.inflate(self.infl_rect[0], self.infl_rect[1]) 

