import vectorlib
from vectorlib import Vector2
from target import Target
import pygame
from constants import *
class Agent(object):
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.mass = 1
        self.force = Vector2(0, 0)
        self.heading = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxvelocity = Vector2(10, 10)

    def seek(self, seektarget):
        self.velocity = Vector2.normalise(seektarget.velocity - self.velocity) * self.maxvelocity
        self.force = self.velocity - self.maxvelocity
        
        
    def update(self, deltatime):
        '''update agent'''
        self.velocity = self.velocity + self.force * deltatime
        # self.position = self.position + self.velocity * deltatime
        # self.heading = Vector2.normalise(self.velocity)
        
    def draw(self, screen):
        pygame.draw.circle(screen, BLACK , [int(self.position.posx), int(self.position.posy)], 25)
        
       

if __name__ == '__main__':
    import main as Main
    Main.main()
        