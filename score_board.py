import pygame

class ScoreBoard:
    def __init__(self, screen):
        self.screen = screen
        # None uses the default Pygame font. 36 is the font size.
        self.font = pygame.font.Font(None, 36) 
        
        # Track your stats here
        self.carrots_eaten = 0
        self.carrots_picked = 0
        self.carrots_saved = 0
        self.coins = 10
        
    def draw(self):
        # Render text into a surface. True is for anti-aliasing. (255,255,255) is white.
        eaten_text = self.font.render(f"Carrots Eaten: {self.carrots_eaten}", True, (255, 255, 255))
        harvest_text = self.font.render(f"Carrots Picked: {self.carrots_picked}", True, (255, 255, 255))
        saved_text = self.font.render(f"Carrots Saved: {self.carrots_saved}", True, (255, 255, 255))
        coins_text = self.font.render(f"Coins: {self.coins}", True, (255, 255, 255))

        # Draw to the top-left corner
        self.screen.blit(eaten_text, (10, 10))
        self.screen.blit(harvest_text, (10, 50))
        self.screen.blit(saved_text, (10, 90))
        self.screen.blit(coins_text, (10, 130))