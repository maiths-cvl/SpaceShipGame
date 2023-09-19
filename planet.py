import pygame
import random

class Planet:
    def __init__(self):
        self.loc = [] # x then y
        self.size = 0
        self.destroys()

    def destroys(self):
        self.loc = [random.randint(50, 1030), random.randint(100, 135)]
        self.size = random.randint(10, 50)