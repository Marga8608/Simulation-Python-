from creature import Creature
import pygame

class Player(Creature):
    def __init__(self, ai_settings, screen, x, y):
        # Pass herbivore-specific attributes to Creature
        stats = {
            "x": x,
            "y": y,
            "sprite_sheet": 'graphics/shura8.png',
            "animation_steps": [8, 8, 8, 8],
            "animation_rows": [2, 3, 1, 0],
            "frame_size_x": 64,
            "frame_size_y": 64,
            "height": 96,
            "width": 96,
            "energy": 100,
            "speed": 90,
            "inflate_rect": [-35,-35]
            }
        super().__init__(ai_settings, screen, **stats)
      
    def update(self, herbs, dt):
        current_time = pygame.time.get_ticks()  
        hits = pygame.sprite.spritecollide(self, herbs, False, 
            collided=lambda s1, s2: s1.hitbox.colliderect(s2.hitbox))
        if hits:
            for hit in hits:             
                overlap_vector = self.pos - hit.pos
                if overlap_vector.length() > 0:
                    overlap_vector = overlap_vector.normalize()
                    hit.pos -= overlap_vector*4
                    hit.hitbox.center = (round(hit.pos.x), round(hit.pos.y))
                hit.angle = self.vel.as_polar()[1]
                hit.escaping = True
                hit.updated = current_time
        else:    
            self.vel.update(0, 0)
            #Update position based on movement flags and speed.
            if self.moving_right and self.hitbox.right < self.screen_rect.right:
                self.vel.x += self.speed
            if self.moving_left and self.hitbox.left > 0:
                self.vel.x -= self.speed
            if self.moving_up and self.hitbox.top > 0:
                self.vel.y -= self.speed
            if self.moving_down and self.hitbox.bottom < self.screen_rect.bottom:
                self.vel.y += self.speed
            #Prevent diagonal speed boosting
            if self.vel.length() > 0:
                self.vel.scale_to_length(self.speed)
            # Sync integer screen rect with precise float tracking     
        
            self.pos += self.vel * dt
            self.hitbox.center = (round(self.pos.x), round(self.pos.y))
            self.animate(current_time) 
            self.rect.midbottom = self.hitbox.midbottom
        
        
          