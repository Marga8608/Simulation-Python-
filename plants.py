class Plant(Creature):
    def __init__(self, ai_settings, screen, x, y):
        stats = {
                    "sprite_sheet": 'graphics/slime.png',
                    "animation_steps": [6, 6, 6, 6],
                    "animation_rows": [3, 4, 4, 5],
                    "frame_size_x": 32,
                    "frame_size_y": 32,
                    "height": 64,
                    "width": 64,
                    "energy": 100,
                    "speed": 0,
                    "inflate_rect": [-40,-40],
                    
                    }
        super().__init__(ai_settings, screen, **stats, x=x, y=y)