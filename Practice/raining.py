import pygame
import sys
from raindrop import Raindrop
class Rain:
    def __init__(self) -> None:
        pygame.init()
        self.screen_width = 1200
        self.screen_height =900
        self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        pygame.display.set_caption('Raining')
        self.color = [230,230,230]
        self.raindrops = pygame.sprite.Group()
        self._create_fleet()
        
    def run_game(self):
        while True:
            
            #self.update_raindrops()
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def update_screen(self):
        self.screen.fill(self.color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def update_raindrops(self):
        pass
        #self.check_edge()
        # self.raindrops.update()
    
    def _create_fleet(self):
        raindrop = Raindrop(self)
        raindrop_width = raindrop.rect.width
        raindrop_height = raindrop.rect.height
        number_raindrops = self.screen_width // (2* raindrop_width)
        number_rows = self.screen_height //(2* raindrop_height)

        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops):
                self._create_raindrop(raindrop_number,row_number)

    def _create_raindrop(self, raindrop_number,row_number):
        raindrop = Raindrop(self)
        raindrop_width,raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width*raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.rect.height + 2* raindrop.rect.height * row_number
        self.raindrops.add(raindrop)

if __name__ == '__main__':
    raining = Rain()
    raining.run_game()