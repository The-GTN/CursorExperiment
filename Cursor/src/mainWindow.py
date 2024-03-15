from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.BubbleWidget import BubbleWidget
from src.NormalWidget import NormalWidget
from src.RopeCursor import RopeCursor
from src.HighLightCursor import HighLightCursor

class MainWindow(QMainWindow):

    def __init__(self,name="BubbleCursor"):
        super().__init__()
        self.setWindowIcon(QIcon('media/logo.png'))
        self.setWindowTitle(name)
        self.bubbleMode()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Space, Qt.Key_Enter, Qt.Key_M]:
            self.changeMode()
        event.accept()

    def changeMode(self):
        if self.mode == "Bubble":
            self.ropeMode()
        elif self.mode == "Rope":
            self.highLightMode()
        elif self.mode == "High":
            self.noneMode()
        else:
            self.bubbleMode()


    def bubbleMode(self):
        self.mode = "Bubble"
        self.setWindowTitle("BubbleCursor")
        self.widget = BubbleWidget()
        self.setCentralWidget(self.widget)

    def ropeMode(self):
        self.mode = "Rope"
        self.setWindowTitle("RopeCursor")
        self.widget.setCursor(RopeCursor)

    def highLightMode(self):
        self.mode = "High"
        self.setWindowTitle("HighLightCursor")
        self.widget.setCursor(HighLightCursor)

    def noneMode(self):
        self.mode = "Normal"
        self.setWindowTitle("NormalCursor")
        self.widget = NormalWidget()
        self.setCentralWidget(self.widget)