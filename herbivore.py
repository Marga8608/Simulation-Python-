from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, screen, player, x, y, score, *groups):
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
        super().__init__(screen, **stats)
        
        self.angle = random.uniform(0,360)
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        self.score = score
        self.state = "searching"
        self.target = None
        
        

    def update(self, dt): 
        current_time = pygame.time.get_ticks() 
        if self.state == "escaping" or self.state == "startled":
            if current_time - self.updated >= self.interval:
                self.state = "searching"              
            else:
                if self.state == "escaping":
                    self.speed = 150
                else:
                    self.speed = 100      
        else:  
                    
            if self.state == "searching":    
                self.speed = self.normal_speed             
                targets = self.check_plants()
                if targets:
                    for target in targets:
                        if target.state == "ready":
                            self.target = target
                            self.state = "targetting"
                            self.speed = 100
                            direction = target.pos - self.pos
                            self.angle = direction.as_polar()[1]
                            break
            elif self.state == "targetting":
                if self.target is not None:
                    direction = self.target.pos - self.pos
                    self.angle = direction.as_polar()[1]    
                    if self.target.state == "ready":
                        if self.hitbox.colliderect(self.target.hitbox):
                            self.state = "escaping"
                            self.target.state = "empty"
                            self.target = None 
                            self.updated = current_time
                            self.score.carrots_eaten += 1
                else:
                    self.state = "searching"
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

    def to_dict(self):
            return {
                "x": self.pos.x,
                "y": self.pos.y,
                "vel_x": self.vel.x,
                "vel_y" : self.vel.y,
                "state" : self.state
            }
