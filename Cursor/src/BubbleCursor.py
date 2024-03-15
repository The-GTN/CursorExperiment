from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import math
from src.NormalCursor import NormalCursor

class BubbleCursor(NormalCursor):

    def __init__(self,targets):
        super().__init__(targets)
        self.defaultCol = QColor(Qt.green)
        self.condition = lambda x : True

    def paint(self,QPainter):
        color = self.defaultCol

        size = self.size * 2

        QPainter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        QPainter.setBrush(QBrush(color, Qt.SolidPattern))
        QPainter.drawEllipse(self.x-self.size,self.y-self.size,size,size)


    