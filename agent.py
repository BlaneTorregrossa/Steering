import vectorlib
from vectorlib import Vector2
from target import Target
import pygame
from constants import *
import gametemplate

class Agent(object):
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.force = Vector2(0, 0)
        self.heading = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxvelocity = 50
        self.currentvelocity = self.velocity
        

    def seek(self, seektarget):
        self.velocity = Vector2.normalise(seektarget.position - self.position) * self.maxvelocity
        self.force = self.velocity - self.currentvelocity
        self.update()

    def flee(self, fleetarget):
        self.velocity = Vector2.normalise(self.position - fleetarget.position) * self.maxvelocity
        self.force = self.velocity - self.currentvelocity
        

    def update(self, deltatime):
        '''update agent'''
        self.position += self.velocity * deltatime
        self.velocity += self.force * deltatime
        self.heading = Vector2.normalise(self.velocity)
        
    def draw(self, screen):
        pygame.draw.circle(screen, BLACK , [int(self.position.posx), int(self.position.posy)], 25)
        

if __name__ == '__main__':
    import main as Main
    Main.main()
        