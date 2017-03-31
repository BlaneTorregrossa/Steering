import vectorlib
from vectorlib import Vector2
import pygame
from constants import *

class Target(object):
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.force = Vector2(0, 0)
        self.heading = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxvelocity = 50
        self.currentvelocity = self.velocity



    def update(self, deltatime):
        '''update agent'''
        self.position = self.position + self.velocity * deltatime

        
    def draw(self, screen):
        pygame.draw.circle(screen, BLACK , [int(self.position.posx), int(self.position.posy)], 10)
        
       

if __name__ == '__main__':
    import main as Main
    Main.main()