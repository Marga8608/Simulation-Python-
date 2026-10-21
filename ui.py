import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, border_radius=8)
        text_surf = self.font.render(self.text, True, "black")
        screen.blit(text_surf, (self.rect.centerx - text_surf.get_width() // 2, 
            self.rect.centery - text_surf.get_height() // 2))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
def start(screen, buttons):
    title_font = pygame.font.Font(None, 64)
    instruction_font = pygame.font.Font(None, 32)
    screen.fill("darkolivegreen")
    # Title & Instructions
    title_surf = title_font.render("Farming Sim", True, "black")
    screen.blit(title_surf, (screen.get_width() // 2 - title_surf.get_width() // 2, 150))
        
    inst_surf = instruction_font.render("Plant and harvest carrots with E and keep the bunnies away!", True, "black")
    screen.blit(inst_surf, (screen.get_width() // 2 - inst_surf.get_width() // 2, 230))
    
    for button in buttons.values():
        button.draw(screen)

    pygame.display.flip()

def game_over(screen):
    game_over_font = pygame.font.Font(None, 74)
    screen.fill("black")
    text_surface = game_over_font.render("You Are Out of Coins!", True, "red")
    
    screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2 - 50))
    pygame.display.flip()