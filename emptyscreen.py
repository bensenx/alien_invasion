import sys
import pygame
size = width,height =1000,800
black = 0,0,0
class Emptyscren:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Empty')
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.text = self.font.render('a',True,(0,255,0), (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (1000//2,800//2)

    def show_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type ==pygame.KEYDOWN:

                    self.text = self.font.render(str(event.key),True,(0,255,0), (0,0,0))
                    self.text_rect = self.text.get_rect()
                    self.text_rect.center = (1000//2,800//2)
                    
            self.screen.fill(black)
            
            self.screen.blit(self.text,self.text_rect)
            pygame.display.flip()

if __name__ == '__main__':
    screen = Emptyscren()
    screen.show_screen()