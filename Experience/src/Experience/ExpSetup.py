from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.Cursor.BubbleWidget import BubbleWidget
from src.Cursor.NormalCursor import NormalCursor
from src.Cursor.HighLightCursor import HighLightCursor
from src.Cursor.BubbleCursor import BubbleCursor
from src.Cursor.RopeCursor import RopeCursor

class ExpSetup(QDialog):

    def __init__(self,window):
        super().__init__()
        self.setWindowTitle("Setup Experience")
        self.setWindowIcon(QIcon('media/images/logo.png'))
        self.setWindowModality(Qt.ApplicationModal)
        self.window = window
        self.finish = False
        self.opts = {"user":"0","technique":"All","densite":3,"size":3,"repetition":4}
        self.initLayout()
        self.exec_()

    def startXP(self):
        self.window.setWidget(BubbleWidget,self.opts)
        self.finish = True
        self.close()

    def initLayout(self):
        self.resize(250,250)

        
        user, label = self.LineInput("user","Numéro d'Utilisateur")
        tech, techlab = self.ChoiceInput("technique","Technique Utilisée") 
        dens, denslab = self.SliderInput("densite","densités")
        taille, taillelab = self.SliderInput("size","tailles de cibles")
        rep, replab = self.SliderInput("repetition","répétitions")
        b = QPushButton("Valider",self)
        b.clicked.connect(self.startXP)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label)
        vbox.addWidget(user)
        vbox.addWidget(techlab)
        vbox.addWidget(tech)
        vbox.addWidget(denslab)
        vbox.addWidget(dens)
        vbox.addWidget(taillelab)
        vbox.addWidget(taille)
        vbox.addWidget(replab)
        vbox.addWidget(rep)
        vbox.addWidget(b)

        self.setLayout(vbox)

    def LineInput(self,att,name):
        label = self.createLabel(name,self.opts[att])
        user = QLineEdit(self)
        user.setText("0")
        user.textChanged[str].connect(lambda v : self.updateLabel(label,att,name,v))
        return (user,label)

    def ChoiceInput(self,att,name):
        cb = QComboBox()
        cb.addItems(["All","Bubble Cursor", "HighLight Cursor", "Normal Cursor", "Rope Cursor"])
        label = self.createLabel(name,cb.currentText())
        cb.currentIndexChanged.connect(lambda _ : self.setCursor(cb.currentText(),label))
        return (cb,label)

    def SliderInput(self,att,name):
        slider = QSlider(Qt.Horizontal, self)
        slider.setRange(1, 10)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setPageStep(5)
        slider.setValue(self.opts[att])

        label = self.createLabel('Nombre de '+name,str(self.opts[att]))

        slider.valueChanged.connect(lambda v : self.updateLabel(label,att,"Nombre de "+name,v))

        return (slider,label)

    def createLabel(self,name,value):
        label = QLabel(name+' : '+value, self)
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label.setMinimumWidth(80)
        return label

    def updateLabel(self,label,att,text,value,setValue=True):
        label.setText(text+" : "+str(value))
        if setValue:
            self.opts[att] = value

    def setCursor(self,text,label):
        self.updateLabel(label,"technique","Technique Utilisée",text,False)
        if text == "Bubble Cursor":
            self.opts["technique"] = BubbleCursor
        elif text == "HighLight Cursor":
            self.opts["technique"] = HighLightCursor
        elif text == "Rope Cursor":
            self.opts["technique"] = RopeCursor
        elif text == "All":
            self.opts["technique"] = "All"
        else:
            self.opts["technique"] = NormalCursor

    def closeEvent(self, event):
        if self.finish:
            event.accept()
        else:
            reply = QMessageBox.question(self, 'Stop Setup', 'Are you sure you want to stop the experiment setup ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.window.error()
                event.accept()
            else:
                event.ignore()

    def event(self, event): 
        if event.type() == QEvent.EnterWhatsThisMode:
            print("Need Help ?")
            QWhatsThis.leaveWhatsThisMode()
            return True
        return QDialog.event(self, event)