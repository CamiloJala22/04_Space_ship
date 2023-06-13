import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    X_POS = ( SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    size_spaceship = [40, 60]

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.size_spaceship[0], self.size_spaceship[1]))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x = self.rect.x - 10
        #Si la nave es = 0, entonces se cambia por el valor que tiene la pantanlla en el eje x
        else: 
             self.rect.x = SCREEN_WIDTH #Menos para que no se esconda
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x = self.rect.x + 10
        #Igual que el la linea 20 pero al rebes 
        else: 
            self.rect.x = -self.size_spaceship[0]
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2: 
            self.rect.y = self.rect.y - 10
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70: 
            self.rect.y = self.rect.y + 10

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))