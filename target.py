import random

import pygame

import gametemplate
import vectorlib
from centertarget import CenterTarget
from constants import *
from gametemplate import GameTemplate
from vectorlib import Vector2


class Target(object):
    def __init__ (self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.heading = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)       #not used
        self.maxvelocity = 10
        self.mass = 1                           #not used

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
        self.velocity += self.force * deltatime
        self.position += self.velocity * deltatime
        if self.position.posx == range(399 - 401):
            if self.position.posy == range(299 - 301):
                self.velocity = Vector2(0, 0)
                self.force = Vector2(0, 0)
        else:
            self.seek(CenterTarget(Vector2(400, 300)))
        print "target pos:", str(self.position.posx), str(self.position.posy)
        print "target vel:", str(self.velocity.posx), str(self.velocity.posy)
        print "target force:", str(self.force.posx), str(self.force.posy)


        
    def draw(self, screen):
        pygame.draw.circle(screen, BLUE , [int(self.position.posx), int(self.position.posy)], 10)
       

if __name__ == '__main__':
    import main as Main
    Main.main()
