from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.NormalCursor import NormalCursor

class RopeCursor(NormalCursor):

    def __init__(self,targets):
        super().__init__(targets)
        self.defaultCol = QColor(Qt.black)
        self.condition = lambda x : True

    def paint(self,QPainter):
        color = self.defaultCol

        QPainter.setPen(QPen(color, 3, Qt.SolidLine))

        if self.closest != None:
            dist = self.closest.size / 2
            if self.closest.x >= self.x:
                dx = -dist
            else:
                dx = dist
            if self.closest.y >= self.y:
                dy = -dist
            else:
                dy = dist
            QPainter.drawLine(self.x, self.y, self.closest.x, self.closest.y)