from sqlite3 import Cursor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import csv
import random
import time

from src.Target import Target
from src.BubbleCursor import BubbleCursor

class BubbleWidget(QWidget):
    
    def __init__(self,cursor=BubbleCursor,file="./media/src_tp_bubble.csv"):
        super().__init__()
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        self.targetsFromFile(file)
        self.cursor = cursor(self.targets)
        self.setTheOneToSelect()
        self.time = time.time()

    def setCursor(self,cursor):
        self.cursor = cursor(self.targets)

    def mouseMoveEvent(self, event): # evenement mouseMove
        self.cursorPos = event.pos() # on stocke la position du curseur
        self.update() # on met à jour l'affichage

    def mousePressEvent(self, event: QMouseEvent) -> None:
        event.accept()
        if self.cursor.closest != None:
            #print("Target Clicked !")
            #print("x : "+str(self.cursor.closest.x)+" | y : "+str(self.cursor.closest.y))
            if self.cursor.closest.toSelect:
                t = time.time()
                print(f'Time : {t-self.time:.3f}sec ')
                self.time = t
                self.cursor.closest.toSelect = False
                self.setTheOneToSelect()
            else:
                print("Oops, it's not the bubble to select !")
    
    #evenement QPaintEvent
    def paintEvent(self, event):
        painter = QPainter(self)

        if self.cursorPos != None:
            self.cursor.move(self.cursorPos.x(),self.cursorPos.y())
            self.cursor.paint(painter)

        for target in self.targets:
            target.paint(painter)

    def targetsFromFile(self,file):
        self.targets = []
        try:
            with open(file, newline='\n') as csvfile:
                read = csv.reader(csvfile, delimiter=',')
                for data in read:
                    self.targets.append(Target(int(data[0]),int(data[1]),int(data[2])))
        except Exception:
            print("Error reading csv file, no target added")

    def setTheOneToSelect(self):
        if len(self.targets) > 0:
            theOne = random.choice(self.targets)
            theOne.toSelect = True

        

    
