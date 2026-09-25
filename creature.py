import pygame
import random

class Creature(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, x=None, y=None,**stats):
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
        self.animation_list = self.load_frames()
        crit_image = self.animation_list[0][0]
        self.image = pygame.transform.scale(crit_image, (self.width, self.height))  
        
        self.animation_cooldown = 200

        #Directions: 0 - Down , 1 - Right, 2 - Left, 3 - Up
        #Corresponds to the rows on the sprite sheet for each movement
        self.direction = 0
        self.current_frame = 0
        self.animation_timer = pygame.time.get_ticks()
        
        #Position setup (default to screen center if x, y are not provided)
        start_x = x if x is not None else self.screen_rect.centerx
        start_y = y if y is not None else self.screen_rect.centery
        self.pos = pygame.math.Vector2(start_x, start_y)
        self.vel = pygame.math.Vector2()
        self.rect = self.image.get_rect()
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.last_update = pygame.time.get_ticks()
        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
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
        if self.vel:
            if abs(self.vel.x) > abs(self.vel.y):
                self.direction = 1 if self.vel.x > 0 else 2
            else:
                self.direction = 0 if self.vel.y > 0 else 3
        else:
            self.direction = 0
        if current_time - self.animation_timer >= self.animation_cooldown:
            self.animation_timer = current_time   
        # Get the list of frames for the current direction
            frame_list = self.animation_list[self.direction]
        # Advance the frame, use modulo (%) to loop back to 0 automatically
            self.current_frame = (self.current_frame + 1) % len(frame_list) 
        # Set the actual sprite image Pygame uses to draw
            self.image = pygame.transform.scale(frame_list[self.current_frame], (self.width, self.height))
    
    #Loads all the animation frames for the object, using get_image on the sheet       
    def load_frames(self):
        complete_list = []
        for i in range(len(self.rows)):          
            temp_list = []
            for j in range(self.steps[i]):
                temp_list.append(self.get_image(j, self.rows[i], self.size_x, self.size_y))
            complete_list.append(temp_list)
        complete_list[2] = [pygame.transform.flip(frame, True, False) for frame in complete_list[1]]
        return(complete_list)

    def get_image(self, col, row, width, height):
        x = col * width
        y = row * height
        rect = pygame.Rect(x, y, width, height)
        return self.sheet.subsurface(rect)

    