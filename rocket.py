import sys
import pygame
black = 0,0,0
size = width,height = 1300,800
class Ball:
    def __init__(self,program) -> None:
        self.ball = pygame.image.load('images\intro_ball.gif')
        self.ball_rect = self.ball.get_rect()
        self.screen_rect = program.screen.get_rect()
        self.ball_rect.center = self.screen_rect.center
    def moving_left(self):
        self.ball_rect.x -= 200
    def moving_right(self):
        self.ball_rect.x += 200
    def blitme(self):
        program.screen.blit(self.ball,self.ball_rect)
class Rocket:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Rocket")
        self.ball = Ball(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.ball.ball_rect.left > self.ball.screen_rect.left:
                        self.ball.moving_left()
                    if event.key == pygame.K_RIGHT and self.ball.ball_rect.right < self.ball.screen_rect.right:
                        self.ball.moving_right()
            self.screen.fill(black)
            self.ball.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    program = Rocket()
    program.run_game()