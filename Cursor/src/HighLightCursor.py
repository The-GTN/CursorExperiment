from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.NormalCursor import NormalCursor

class HighLightCursor(NormalCursor):

    def __init__(self,targets):
        super().__init__(targets)
        self.defaultCol = QColor(Qt.black)
        self.condition = lambda x : True

    def paint(self,QPainter):
        pass