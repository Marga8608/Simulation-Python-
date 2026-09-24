from creature import Creature
import pygame
import random

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, all_herbs, x, y):
        # Pass herbivore-specific image and coordinates to base Creature
        super().__init__(ai_settings, screen, x=x, y=y)

        self.sheet = pygame.image.load('graphics/slime.png').convert_alpha()
        self.animation_list = []
        animation_steps = [6, 6, 6, 6]
        animation_rows = [3, 4, 4, 5]
        last_update = pygame.time.get_ticks()
        self.animation_cooldown = 200
        self.direction = 'down'
        self.current_frame = 0
        self.animation_timer = pygame.time.get_ticks()

        for i in range(len(animation_rows)):
            temp_image_list = []
            for j in range(animation_steps[i]):
                temp_image_list.append(self.get_image(j, animation_rows[i], 32, 32))
            self.animation_list.append(temp_image_list)

        # Herbivore-specific attributes
        crit_image = self.animation_list[0][0]
        self.image = pygame.transform.scale(crit_image, (self.width, self.height))
        self.energy = 100
        self.herb_group = all_herbs
        self.speed = random.uniform(0,0.3)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.angle = random.uniform(0,360)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.speed, self.angle))
        self.updated = pygame.time.get_ticks()
        self.interval = random.randint(1500, 4000)

    def get_image(self, col, row, width, height):
        x = col * width
        y = row * height
        rect = pygame.Rect(x, y, width, height)
        return self.sheet.subsurface(rect)

    def update(self): 
        current_time = pygame.time.get_ticks()
        current_speed = self.vel.length()
    
    # 2. Prevent division by zero if the herbivore stops moving

        if abs(self.vel.x) > abs(self.vel.y):
            self.direction = 1 if self.vel.x > 0 else 2
        else:
            self.direction = 0 if self.vel.y > 0 else 3

        if current_time - self.animation_timer >= self.animation_cooldown:
            self.animation_timer = current_time   
        # Get the list of frames for the current direction
            frame_list = self.animation_list[self.direction]
        # Advance the frame, use modulo (%) to loop back to 0 automatically
            self.current_frame = (self.current_frame + 1) % len(frame_list) 
        # Set the actual sprite image Pygame uses to draw
            self.image = pygame.transform.scale(frame_list[self.current_frame], (self.width, self.height))
        
        '''if current_time - self.updated >= self.interval:
            self.update_velocity()
            self.updated = current_time
            self.interval = random.randint(1500, 10000)
            self.speed = random.uniform(0,0.3) '''
        # Check X boundaries (Left and Right)
        if self.rect.left <= 0 or self.rect.right >= self.ai_settings.screen_width:
            self.vel.x *= -1  # Reverses horizontal direction instantly 
        # Check Y boundaries (Top and Bottom)
        if self.rect.top <= 0 or self.rect.bottom >= self.ai_settings.screen_height:
            self.vel.y *= -1  # Reverses vertical direction instantly
        if self.vel.x == 0 or self.vel.y == 0:
            self.update_velocity()
        self.update_flag()
            #Update position based on movement flags and speed.
        if self.moving_right:
            self.pos.x += self.vel.x
        if self.moving_left:
            self.pos.x += self.vel.x
        if self.moving_up:
            self.pos.y += self.vel.y
        if self.moving_down:
            self.pos.y += self.vel.y
        # Sync integer screen rect with precise float tracking
        self.rect.center = (round(self.pos.x), round(self.pos.y))