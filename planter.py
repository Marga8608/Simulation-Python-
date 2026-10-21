from static_object import Static_object
import pygame

class Planter(Static_object):
    def __init__(self, screen,  x, y, *groups):
        stats = {
            "x": x,
            "y": y,
            "height": 64,
            "width": 64,
            "image": "graphics/planter.png",
            "inflate_rect": [-10,-10]
        }
        super().__init__(screen, **stats)
        empty_img = pygame.image.load("graphics/empty.png").convert_alpha()
        planted_img = pygame.image.load("graphics/planted.png").convert_alpha()
        growing_img = pygame.image.load("graphics/growing.png").convert_alpha()
        ready_img = pygame.image.load("graphics/ready.png").convert_alpha()
        self.empty_img = pygame.transform.scale(empty_img, (self.width, self.height))
        self.growing_img = pygame.transform.scale(growing_img, (self.width, self.height))
        self.ready_img = pygame.transform.scale(ready_img, (self.width, self.height))
        self.planted_img = pygame.transform.scale(planted_img, (self.width, self.height))
        self.state = "empty"
        self.grow_timer = 0
        self.grow_time = 10.0  # Time in seconds for the planter to

    def update(self, dt):
        if self.state == "empty":
            self.image = self.empty_img       
        else:
            if self.state == "planted":
                self.image = self.planted_img  
                self.grow_timer += dt
                if self.grow_timer >= self.grow_time:                 
                    self.state = "growing"
                    self.grow_timer = 0
            elif self.state == "growing":
                self.image = self.growing_img 
                self.grow_timer += dt
                if self.grow_timer >= self.grow_time:
                    self.state = "ready"
                    self.grow_timer = 0
            elif self.state == "ready":
                self.image = self.ready_img  

    def to_dict(self):
            return {
                "x": self.pos.x,
                "y": self.pos.y,

            }