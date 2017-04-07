import random

import pygame

import gametemplate
import vectorlib
from constants import *
from gametemplate import GameTemplate
from vectorlib import Vector2


class CenterTarget(object):
    def __init__ (self, position):
        self.position = position
        self.velocity = Vector2(0, 0)
        self.heading = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxvelocity = 0
        
    def update(self, deltatime):
        t = 0

        
    def draw(self, screen):
        pygame.draw.circle(screen, GREEN , [int(self.position.posx), int(self.position.posy)], 5)
        
       

if __name__ == '__main__':
    import main as Main
    Main.main()
