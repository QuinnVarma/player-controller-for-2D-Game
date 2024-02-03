import pygame
from spritesheet import SpriteSheet

class Object(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = SpriteSheet('./Assets/Textures/Pixel Adventure 1/Free/')
        self.curr_sprite