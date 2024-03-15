from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import csv
import random

from src.Experience.CreateTargets import createCibles, createSequence
from src.Cursor.BubbleWidget import BubbleWidget
from src.Cursor.NormalCursor import NormalCursor
from src.Cursor.BubbleCursor import BubbleCursor
from src.Cursor.RopeCursor import RopeCursor

# createFiles(nbTargets,sizeTarget,minSpace)

MINSPACE = 3

class XPManager:

    def __init__(self,window,opts):
        # {"user":...,"technique":...,"densite":...,"size":...,"repetition":...}
        self.opts = opts
        if opts["technique"] == "All":
            #self.techniques = [BubbleCursor,NormalCursor,HighLightCursor,RopeCursor] 
            self.techniques = [BubbleCursor,NormalCursor,RopeCursor] 
        else:
            self.techniques = [opts["technique"]]
        self.createFiles()
        self.window = window

    def createFiles(self):
        # '../media/terrains/cibles_'+ext
        # ext = str(nbTargets)+'_'+str(sizeTarget)+'_'+str(minSpace)+'.csv'
        files = []
        for t in self.techniques:
            for d in self.getDensite():
                for s in self.getSizes():
                    ext = str(d)+'_'+str(s)+'_'+str(MINSPACE)+'.csv'
                    filecible = './media/terrains/cibles_'+ext
                    fileseq = './media/sequences/sequence_'+ext
                    current = {"fileCible":filecible,"fileseq":fileseq,"densite":d,"size":s,"technique":t}
                    files.append(current)
        random.shuffle(files)
        for f in files:
            try:
                with open(f["fileCible"], newline='\n') as csvfile:
                    read = csv.reader(csvfile, delimiter=',')
            except Exception:
                createCibles(f["fileCible"],f["densite"],f["size"],MINSPACE)
            try:
                with open(f["fileseq"], newline='\n') as csvfile:
                    read = csv.reader(csvfile, delimiter=',')
            except Exception:
                createSequence(f["fileseq"],f["densite"])
        
        self.files = files
        self.currentfile = 0
        self.count = 0


    def setWidget(self,widget):
        file = self.files[self.currentfile]
        self.window.setWindowTitle("Expérience contrôlée : "+str(self.currentfile*self.opts["repetition"])+"/"+str(len(self.files)*self.opts["repetition"]))
        return widget(self.window,file["technique"],file["fileCible"],file["fileseq"])

    def notifyResult(self,id,t,errors):
        file = self.files[self.currentfile]
        d = file["densite"]
        s = file["size"]
        t = float("{:.2f}".format(t))
        filename = './media/resultats/résultats_experience.csv'
        with open(filename, 'a') as f:
            f.write(self.opts["user"]+","+str(id)+","+str(t)+","+str(errors)+","+file["technique"].__name__+","+str(d)+","+str(s))
            f.write('\n')
        self.count += 1
        self.window.setWindowTitle("Expérience contrôlée : "+str(self.currentfile*self.opts["repetition"]+self.count)+"/"+str(len(self.files)*self.opts["repetition"]))
        if self.count >= self.opts["repetition"]:
            self.count = 0
            self.currentfile += 1
            if self.currentfile < len(self.files):
                self.window.setCentralWidget(self.setWidget(BubbleWidget))
            else:
                print("Thanks for doing the experiment !")
                self.window.error()


    def getDensite(self):
        return [30,60,90,20,10,80,50,70,40,42][:self.opts["densite"]]

    def getSizes(self):
        return [6,12,18,5,10,25,7,5,11,8][:self.opts["size"]]