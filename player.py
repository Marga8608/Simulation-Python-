from creature import Creature
import pygame

class Player(Creature):
    def __init__(self, ai_settings, screen, x=None, y=None):
        # Pass herbivore-specific attributes to Creature
        stats = {
            "sprite_sheet": 'graphics/shura.png',
            "animation_steps": [9, 9, 9, 9],
            "animation_rows": [2, 3, 3, 0],
            "frame_size_x": 64,
            "frame_size_y": 64,
            "energy": 100,
            "speed": 0.5
            }
        super().__init__(ai_settings, screen, **stats, x=x, y=y)
      
    def update(self):
        current_time = pygame.time.get_ticks()  
        self.vel.update(0, 0)
        #Update position based on movement flags and speed.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.vel.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.vel.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.vel.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vel.y += self.speed
        #Prevent diagonal speed boosting
        if self.vel.length() > 0:
            self.vel.scale_to_length(self.speed)
        # Sync integer screen rect with precise float tracking
        self.animate(current_time) 
        self.pos += self.vel
        self.rect.center = (round(self.pos.x), round(self.pos.y))
          