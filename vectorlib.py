import math

class Vector2(object):
    def __init__ (self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    def magnitude(self):
        mag = math.sqrt((self.posx * self.posx) + (self.posy * self.posy))
        return mag

    def normalise(self):
        return Vector2((self.posx / self.magnitude()), (self.posy / self.magnitude()))

    def dotprod(self, rhs):
        dot = self.posx * rhs.posx + self.posy * rhs.posy
        return dot

    def scalrmult (self, scalrval):
        prod = (self.posx * scalrval) + (self.posy * scalrval)
        return prod

    def add (self, rhs):
        return Vector2(self.posx + rhs.posx, self.posy + rhs.posy)

    def sub (self, rhs):
        return Vector2(self.posx - rhs.posx, self.posy - rhs.posy)
    
    def mult (self, rhs):
        return Vector2(self.posx * rhs.posx, self.posy * rhs.posy)

    def divi (self, rhs):
        return Vector2(self.posx / rhs.posx, self.posy / rhs.posy) 
    
    def __add__(self, other):
        return self.add(other)
    def __sub__(self, other):
        return self.sub(other)
    def __mul__(self, scalar):
        return Vector2(self.posx * scalar, self.posy * scalar)
        

if __name__ == '__main__':
    import main as Main
    Main.main()