class Settings():
    #Initialize the game's settings.
    def __init__(self):
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = ("forestgreen")
        self.caption = ("Simulation")

        #Crit settings
        self.crit_speed = 0
        self.crit_image = 'graphics/carn.png'

        #Herb settings
        self.herb_image = 'graphics/herb.png'
