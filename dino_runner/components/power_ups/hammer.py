import random
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)
        self.rect.y = 250
        self.index = 0
        
