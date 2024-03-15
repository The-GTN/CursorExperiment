from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import math

class NormalCursor():

    def __init__(self,targets):
        self.x = 0
        self.y = 0 
        self.targets = targets
        self.size = 1000000
        self.closest = None
        self.condition = lambda x: x <=5

    def paint(self,QPainter):
        QPainter.drawEllipse(\
            self.x-5,\
            self.y-5,10,10)

    def move(self,x,y):
        self.x = x
        self.y = y
        if self.closest != None:
            self.closest.highlighted = False
        self.closest = None
        self.size = 1000000

        if len(self.targets) > 0:
            for target in self.targets:
                tx = target.x
                ty = target.y
                dist = math.sqrt((tx-self.x)**2 + (ty-self.y)**2)
                dist = dist-(target.size/2)
                if dist < self.size and self.condition(dist):
                    self.closest = target
                    self.size = dist

        if self.closest != None:
            self.closest.highlighted = True