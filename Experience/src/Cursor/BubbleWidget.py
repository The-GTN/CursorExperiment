from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import csv
import random
import time

from src.Cursor.Target import Target
from src.Cursor.BubbleCursor import BubbleCursor
from src.Cursor.NormalCursor import NormalCursor
from src.Cursor.RopeCursor import RopeCursor

class BubbleWidget(QWidget):
    
    def __init__(self,window,cursor=BubbleCursor,file="./media/terrains/src_tp_bubble.csv",seqfile=None):
        super().__init__()
        self.window = window
        self.setMouseTracking(True) # on active le mouseTracking
        self.cursorPos = None
        self.targetsFromFile(file)
        self.cursor = cursor(self.targets)
        self.setSequence(seqfile,cursor)
        self.setTheOneToSelect()
        self.time = time.time()
        self.nbErrors = 0

    def setSequence(self,seqfile,cursor):
        if seqfile != None:
            try:
                with open(seqfile, newline='\n') as csvfile:
                    read = csv.reader(csvfile, delimiter=',')
                    sequence = []
                    for data in read:
                        sequence.append(int(data[0]))
                    i = 0
                    #if self.cursor == BubbleCursor:
                    #    i += 11%len(sequence)
                    #elif self.cursor == RopeCursor:
                    #    i += 23%len(sequence)
                    self.sequence = [sequence,i]
                    #self.sequence = [sequence,random.randint(0,len(sequence)-1)]
            except Exception:
                self.sequence = None
                print("Error reading csv file, no sequence used")
        else:
            self.sequence = seqfile


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
                save_t = t-self.time
                #print(f'Time : {t-self.time:.3f}sec ')
                self.time = t
                self.cursor.closest.toSelect = False
                self.setTheOneToSelect(save_t)
                self.nbErrors = 0
            else:
                self.nbErrors += 1
                self.errorDialog()
                #print("Oops, it's not the bubble to select !")
        else:
            self.nbErrors += 1
            self.errorDialog()
    
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

    def setTheOneToSelect(self,t=None):
        if len(self.targets) > 0:
            if self.sequence == None:
                theOne = random.choice(self.targets)
                theOne.toSelect = True
            else:
                i = self.sequence[1]
                seq = self.sequence[0]
                theOne = self.targets[seq[i]]
                theOne.toSelect = True
                self.sequence[1] = (self.sequence[1] + 1)%len(self.sequence[0])
                if self.window.manager != None and t != None:
                    self.window.manager.notifyResult(seq[i],t,self.nbErrors)

    def errorDialog(self):
        error = QDialog()
        error.setWindowTitle("Error")
        error.setWindowIcon(QIcon('media/images/logo.png'))
        error.setWindowModality(Qt.ApplicationModal)
        vbox = QVBoxLayout()
        b = QPushButton("Sorry",self)
        b.clicked.connect(error.close)
        label = QLabel("Oops ! You made a mistake !", error)
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label.setMinimumWidth(80)
        vbox.addWidget(label)
        vbox.addWidget(b)
        error.setLayout(vbox)
        error.exec_()



        

    
