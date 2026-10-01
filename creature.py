import pygame
import random

class Creature(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, **stats):
        # 1. Initialize Pygame's Sprite parent class
        super().__init__()
        #Screen settings
        self.screen = screen 
        self.ai_settings = ai_settings 
        self.screen_rect = self.screen.get_rect()
        #Sprite 
        sheet = stats.get("sprite_sheet")       
        self.sheet = pygame.image.load(sheet).convert_alpha()             
        self.size_x = stats.get("frame_size_x", 32)
        self.size_y = stats.get("frame_size_y", 32)
        self.height = stats.get("height", 64)
        self.width = stats.get("width", 64)
        self.energy = stats.get("energy", 100)
        self.speed = stats.get("speed", 0.1)
        #Frames
        self.rows = stats.get("animation_rows")
        self.steps = stats.get("animation_steps")
        self.infl_rect = stats.get("inflate_rect")
        self.herbs = stats.get("herbs")
        self.static = stats.get("static_objects")
        self.plants = stats.get("plants")
        self.player = stats.get("player")
        self.updated = pygame.time.get_ticks()
        self.interval = 5000
        self.animation_list = self.load_frames()
        crit_image = self.animation_list[0][0]
        self.image = pygame.transform.scale(crit_image, (self.width, self.height))  
        
        self.animation_cooldown = 200

        #Directions: 0 - Down , 1 - Right, 2 - Left, 3 - Up
        #Corresponds to the rows on the sprite sheet for each movement
        self.direction = 0
        self.current_frame = 0
        self.animation_timer = pygame.time.get_ticks()
        
        #Position setup
        self.pos = pygame.math.Vector2(stats.get("x"), stats.get("y"))
        self.vel = pygame.math.Vector2()
        self.rect = self.image.get_rect()
        self.hitbox = self.rect.inflate(self.infl_rect[0], self.infl_rect[1]) 
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
        self.rect.center = self.hitbox.center
        self.last_update = pygame.time.get_ticks()
        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.escaping = False
        self.startled = False
        #Groups

    def blitme(self):
        #Draw the creature manually (if not using Pygame Group drawing).
        self.screen.blit(self.image, self.rect)

    def update_velocity(self):
            self.angle = random.uniform(0,360)
            self.vel.from_polar((self.speed, self.angle))
    
    def update_flag(self):
        if self.vel.x > 0:
            self.moving_right = True
            self.moving_left = False
        if self.vel.x < 0:
            self.moving_left = True
            self.moving_right = False
        if self.vel.y > 0:
            self.moving_down = True
            self.moving_up = False
        if self.vel.y < 0:
            self.moving_up = True
            self.moving_down = False
 
    def animate(self, current_time):
        speed = self.vel.length()
        if speed > 0:
            if abs(self.vel.x) > abs(self.vel.y):
                self.direction = 1 if self.vel.x > 0 else 2
            else:
                self.direction = 0 if self.vel.y > 0 else 3
            dynamic_cooldown = self.animation_cooldown / (speed * 0.05)
        else:
            dynamic_cooldown = self.animation_cooldown
            self.direction = 0
        if current_time - self.animation_timer >= dynamic_cooldown:
            self.animation_timer = current_time   
        # Get the list of frames for the current direction
            frame_list = self.animation_list[self.direction]
        # Advance the frame, use modulo (%) to loop back to 0 automatically
            self.current_frame = (self.current_frame + 1) % len(frame_list) 
        # Set the actual sprite image Pygame uses to draw
            self.image = pygame.transform.scale(frame_list[self.current_frame], (self.width, self.height))           
            self.rect = self.image.get_rect(center=self.rect.center)
        
    #Loads all the animation frames for the object, using get_image on the sheet       
    def load_frames(self):
        complete_list = []
        for i in range(len(self.rows)):          
            temp_list = []
            for j in range(self.steps[i]):
                temp_list.append(self.get_image(j, self.rows[i], self.size_x, self.size_y))
            complete_list.append(temp_list)
        
        return(complete_list)

    def get_image(self, col, row, width, height):
        x = col * width
        y = row * height
        rect = pygame.Rect(x, y, width, height)
        return self.sheet.subsurface(rect)

    def check_collisions(self, current_time):
        hits = pygame.sprite.spritecollide(self, self.herbs, False, 
        collided=lambda s1, s2: s1 != s2 and s1.hitbox.colliderect(s2.hitbox))
        if hits:
            if not self.escaping:
                self.startled = True
                self.updated = current_time
            target = hits[0]
            target.angle, self.angle = self.vel.as_polar()[1], target.vel.as_polar()[1]
            target.startled = True
            target.updated = current_time
        # Checks for hitbox overlap
            self.check_overlap(target)
               
    def wall_collisions(self):
        hits = pygame.sprite.spritecollide(self, self.static, False, 
        collided=lambda s1, s2: s1 != s2 and s1.hitbox.colliderect(s2.hitbox))
        if hits:
            for hit in hits:
                self.check_overlap(hit)

    def check_overlap(self, other_rect):
        overlap = self.hitbox.clip(other_rect.hitbox)
        if overlap.width < overlap.height:
        # Resolve X axis
            if self.hitbox.centerx < other_rect.hitbox.centerx:
                self.pos.x -= overlap.width
            else:
                self.pos.x += overlap.width
            self.vel.x *= -1 # Reverse velocity for bounce
        else:
        # Resolve Y axis
            if self.hitbox.centery < other_rect.hitbox.centery:
                self.pos.y -= overlap.height
            else:
                self.pos.y += overlap.height
            self.vel.y *= -1 # Reverse velocity for bounce
        self.angle = self.vel.as_polar()[1]
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
            
