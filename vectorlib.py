import math

class Vector2(object):
    def __init__ (self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    def magnitude(self):
        mag = math.sqrt((self.posx * self.posx) + (self.posy * self.posy))
        return mag

    def normalise(self):
        self.posx = (self.posx / Vector2.magnitude())
        self.posy = (self.posy / Vector2.magnitude())

    def dotprod(self):
        dot = self.posx * posx + self.posy * posy
        return dot