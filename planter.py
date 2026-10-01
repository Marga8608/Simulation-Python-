from static_object import Static_object
import pygame

class Planter(Static_object):
    def __init__(self, ai_settings, screen,  x, y, *groups):
        stats = {
            "x": x,
            "y": y,
            "height": 32,
            "width": 32,
            "image": "graphics/planter.png",
        }
        super().__init__(ai_settings, screen, **stats)
        self.empty_img = pygame.image.load("graphics/empty.png").convert_alpha()
        self.planted_img = pygame.image.load("graphics/planted.png").convert_alpha()
        self.growing_img = pygame.image.load("graphics/growing.png").convert_alpha()
        self.ready_img = pygame.image.load("graphics/ready.png").convert_alpha()
        self.empty = True
        self.planted = False
        self.growing = False
        self.ready = False
        self.grow_timer = 0
        self.grow_time = 10.0  # Time in seconds for the planter to

    def update(self, dt):
        if self.empty:
            self.image = pygame.transform.scale(self.empty_img, (self.width, self.height))  
        elif self.planted:
            self.image = pygame.transform.scale(self.planted_img, (self.width, self.height))
        else:
            if self.growing:
                self.image = pygame.transform.scale(self.growing_img, (self.width, self.height))  
                self.grow_timer += dt
                if self.grow_timer >= self.grow_time:
                    self.growing = False
                    self.ready = True
            if self.ready:
                self.image = pygame.transform.scale(self.ready_img, (self.width, self.height))  