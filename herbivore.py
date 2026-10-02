from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, player, x, y, score, *groups):
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
            "plants": groups[3],
            "player": player
            }
        super().__init__(ai_settings, screen, **stats)
        
        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        self.score = score
        self.searching = True
        self.targetting = False
        self.target = None
        self.targ_rect = self.rect.inflate(300, 300)
        

    def update(self, dt): 
        current_time = pygame.time.get_ticks() 
        if self.escaping and current_time - self.updated < self.interval:
                self.speed =150
                self.startled = False
        elif self.startled and current_time - self.updated < self.interval:
                self.speed = 100
        else:  
            self.escaping = False
            self.startled = False
            self.speed = self.normal_speed
            if self.searching:
                target = self.check_plants()
                if target:
                    self.targetting = True
                    self.searching = False
                    self.target = target
                    direction = target.pos - self.pos
                    self.angle = direction.as_polar()[1]
            elif self.targetting:
                direction = self.target.pos - self.pos
                self.angle = direction.as_polar()[1]
                self.speed = 100
                if self.target.ready:
                    if self.hitbox.clip(self.target.hitbox):
                        self.targetting = False
                        self.searching = True
                        self.target.ready = False
                        self.target.empty = True
                        self.escaping = True
                        self.updated = current_time
                        self.score.carrots_eaten += 1
                else:
                     self.targetting = False
                     self.searching = True  
                     self.target = None  
            
        self.vel.from_polar((self.speed, self.angle))
        self.check_walls()

        #self.player_collision()
        self.check_bumps(current_time)
        #Update position based on movement flags and speed.
        self.update_flag()
        #Updates self.angle in case of bouncing off walls!!!
        self.angle = self.vel.as_polar()[1]
        self.pos += self.vel *dt
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
        self.animate(current_time) 
        self.rect.center = self.hitbox.center
