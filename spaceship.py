import pygame

class Spaceship:
    def __init__(self):
        self.hp = 3
        self.speed = 10
        self.damage = 100
        self.pos = [540, 600]
        self.img = pygame.image.load("spaceship.png")