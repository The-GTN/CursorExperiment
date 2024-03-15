from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Dessin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None

    def mouseMoveEvent(self, event): # evenement mouseMove
        self.cursorPos = event.pos() # on stocke la position du curseur
        self.update() # on met à jour l'affichage
    
    #evenement QPaintEvent
    def paintEvent(self, event):
        painter = QPainter(self)
        if self.cursorPos != None:
            painter.drawEllipse(\
            self.cursorPos.x()-5,\
            self.cursorPos.y()-5,10,10)