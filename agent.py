import vectorlib
from vectorlib import Vector2
import pygame
from constants import *
import gametemplate
from gametemplate import GameTemplate

class Agent(object):
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.heading = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxvelocity = 50

    def seek(self, seektarget):
        '''seek command'''
        displacement = Vector2.normalise(seektarget.position - self.position)
        distvector = displacement * self.maxvelocity
        seekforce = distvector - self.velocity
        self.force = seekforce
        return seekforce

    def flee(self, fleetarget):
        '''flee command'''
        displacement = Vector2.normalise(self.position - fleetarget.position)
        distvector = displacement * self.maxvelocity
        fleeforce = distvector - self.velocity
        self.force = fleeforce
        return fleeforce

    def update(self, deltatime):
        '''update agent'''
        self.velocity = self.velocity + self.force * deltatime
        self.position = self.position + self.velocity * deltatime 

    def draw(self, screen):
        '''draws moving agents'''
        pygame.draw.circle(screen, RED , [int(self.position.posx), int(self.position.posy)], 10)
        

if __name__ == '__main__':
    import main as Main
    Main.main()
        