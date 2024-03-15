from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Target():

    def __init__(self,x,y,size):
        self.defaultCol = QColor(Qt.blue)
        self.toSelectCol = QColor(255,10,120,200)
        self.highlightCol = QColor(Qt.red)
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self,QPainter):
        color = self.selectColor()
        QPainter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        QPainter.setBrush(QBrush(color, Qt.SolidPattern))
        QPainter.drawEllipse(self.x-(self.size/2),self.y-(self.size/2),self.size,self.size)

    def selectColor(self):
        if self.highlighted:
            return self.highlightCol
        elif self.toSelect:
            return self.toSelectCol
        else:
            return self.defaultCol