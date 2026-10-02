import pygame

class ScoreBoard:
    def __init__(self, screen, screen_width):
        self.screen = screen
        self.screen_width = screen_width
        # None uses the default Pygame font. 36 is the font size.
        self.font = pygame.font.Font(None, 36) 
        
        # Track your stats here
        self.carrots_eaten = 0
        self.carrots_picked = 0
        self.carrots_saved = 0
        self.coins = 10
        
    def draw(self):
        y_pos = 10
        num = self.screen_width // 4  # Divide the screen width into 4 equal parts for spacing
        # Render text into a surface. True is for anti-aliasing. (255,255,255) is white.
        stats = {
            "Carrot eaten": {self.carrots_eaten}, 
            "Carrots picked": {self.carrots_picked},
            "Carrots saved": {self.carrots_saved}, 
            "Coins": {self.coins}
        }
        num = (self.screen_width - 20) / len(stats)
        # Draw to the top-left corner

        for i, (key, value) in enumerate(stats.items()):
            text_surface = self.font.render(f"{key}: {value}", True, "white", "darkolivegreen")
            self.screen.blit(text_surface, (y_pos + (i * num), y_pos))