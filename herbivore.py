from creature import Creature

class Herbivore(Creature):
    def __init__(self, ai_settings, screen, x, y):
        # Pass herbivore-specific image and coordinates to base Creature
        super().__init__(ai_settings, screen, image_path='graphics/herb.png', x=x, y=y)
        
        # Herbivore-specific attributes
        self.energy = 100