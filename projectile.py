import pygame

class Projectile:
    def __init__(self):
        self.loc = [-100, -100]
        self.destroyState = False

    def update(self):
        if self.destroyState == False:
            self.loc[1] -= 5
        elif self.destroyState == True:
            self.loc = [-100, -100]
