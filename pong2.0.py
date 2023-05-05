import pygame
import sys
from random import randint
from degrees_to_velocuty import degrees_to_velocity


class Game():
    def __init__(self):
        pygame.init()
        WHITE = (255, 255, 255)
        screen_info = pygame.display.Info()
        self.W = screen_info.current_w
        self.H = screen_info.current_h
        self.screen = pygame.display.set_mode(
            (self.W, self.H),
            pygame.FULLSCREEN
        )
        self.screen_rect = self.screen.get_rect()
        self.edge = self.screen_rect.height - self.screen_rect.height * 0.10
        self.player_1 = Paddle(
            self.screen_rect,
            (self.screen_rect.width * 0.1, self.screen_rect.centery),
            WHITE
        )
        self.player_2 = Paddle(
            self.screen_rect,
            (self.screen_rect.width * 0.9, self.screen_rect.centery),
            WHITE
        )
        self.ball = Ball(
            self.screen_rect,
            self.screen_rect.center,
            WHITE
        )
        self.all_sprites = pygame.sprite.Group()  # создаёт группу спрайтов
        self.all_sprites.add(self.player_1)  # добавляет игрока в группу
        self.all_sprites.add(self.player_2)
        self.all_sprites.add(self.ball)

    def main_loop(self, game=True, FPS=30):
        self.FPS = FPS
        clock = pygame.time.Clock()
        self.game = game
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False
            if keys[pygame.K_UP]:  # клавиша стрелка вверх
                if self.player_1.rect.centery:
                    self.player_1.move("up")
            if keys[pygame.K_DOWN]:  # клавиша стрелка вниз
                if self.player_1.rect.centery:
                    self.player_1.move("down")

            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)



class Paddle(pygame.sprite.Sprite):
    def __init__(
            self,
            screen,
            center: tuple,
            color: tuple
    ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (screen.width * 0.01, screen.height * 0.10)
        )
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = center[0]
        self.rect.centery = center[1]

    def move(self, direction):
        if direction == "up":
            self.rect.centery += 1
        if direction == "down":
            self.rect.centery -= 1


class Ball(pygame.sprite.Sprite):
    def __init__(
            self,
            screen,
            center: tuple,
            color: tuple
    ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (10, 10)
        )
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = center[0]
        self.rect.centery = center[1]


game = Game()
game.main_loop()
pygame.quit()
sys.exit()
