from math import sqrt
from random import randint

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    @property
    def mag(self):
        return sqrt(self.x**2+self.y**2)

    def reset(self):
        self.move(0,0)

    def move(self,newx,newy):
        self.x=newx
        self.y=newy

    def movX(self,newx):
        self.x=newx

    def movY(self,newy):
        self.x=newy

    def __repr__(self):
        return f'({self.x},{self.y})'

## Main Program ##


def addPoints(p1,p2):
    return Point(p1.x+p2.x,p1.y+p2.y)


p1 = Point()
p2 = Point(2, 3)
print(repr(p2))