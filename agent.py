import random

import pygame

import gametemplate
import vectorlib
import target
from target import Target
from centertarget import CenterTarget
from constants import *
from gametemplate import GameTemplate
from vectorlib import Vector2



class Agent(object):
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
        '''update for agent'''
        self.velocity += self.force * deltatime
        self.position += self.velocity * deltatime
        self.flee(CenterTarget(Vector2(400, 300)))
        print "agent pos:", str(self.position.posx), str(self.position.posy)
        print "agent vel:", str(self.velocity.posx), str(self.velocity.posy)
        print "agent force:", str(self.force.posx), str(self.force.posy)



    def draw(self, screen):
        '''draws moving agents'''
        pygame.draw.circle(screen, RED , [int(self.position.posx), int(self.position.posy)], 10)

if __name__ == '__main__':
    import main as Main
    Main.main()
