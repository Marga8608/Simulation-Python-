from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, player, x, y, *groups):
        # Pass herbivore-specific attributes to Creature
        stats = {
            "x": x,
            "y": y,
            "sprite_sheet": 'graphics/bunny8.png',
            "animation_steps": [8, 8, 8, 8],
            "animation_rows": [0, 1, 2, 3],
            "frame_size_x": 32,
            "frame_size_y": 32,
            "height": 64,
            "width": 64,
            "energy": 100,
            "speed": random.uniform(10,40),
            "inflate_rect": [-40,-40],
            "herbs": groups[0],
            "static_objects": groups[2],
            "player": player
            }
        super().__init__(ai_settings, screen, **stats)
        
        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        

    def update(self, dt): 
        current_time = pygame.time.get_ticks() 
        if self.escaping and current_time - self.updated < self.interval:
                self.vel.from_polar((150, self.angle))
        elif self.startled and current_time - self.updated < self.interval:
                self.vel.from_polar((100, self.angle))
        else:
            self.vel.from_polar((self.speed, self.angle))
            self.escaping = False
            self.startled = False
        if self.vel.x == 0 or self.vel.y == 0:
            self.update_velocity()
            
        self.wall_collisions()

        #self.player_collision()
        self.check_collisions(current_time)
        #Update position based on movement flags and speed.
        self.update_flag()
        #Updates self.angle in case of bouncing off walls!!!
        self.angle = self.vel.as_polar()[1]
        self.pos += self.vel *dt
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
        self.animate(current_time) 
        self.rect.center = self.hitbox.center
