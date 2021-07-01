import pygame
from pygame.sprite import Sprite
class Raindrop(Sprite):
    def __init__(self,ai_game) -> None:
        
        super().__init__()
        self.screen = ai_game.screen
        image = pygame.image.load('images/raindrop.bmp')
        self.image = pygame.transform.scale(image,(60,40))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
