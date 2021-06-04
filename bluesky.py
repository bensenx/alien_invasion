import pygame
import sys
class Momo:
    def __init__(self,game) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/momo.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)

class BlueSky:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (51,102,255)
        self.momo = Momo(self)
    def show(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.momo.blitme()
            pygame.display.flip()
if __name__ == '__main__':
    blue = BlueSky()
    blue.show()
