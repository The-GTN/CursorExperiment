from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.dessin import *

class MainWindow(QMainWindow):

    def __init__(self,name="TPs PyQt"):
        super().__init__()
        self.setWindowIcon(QIcon('media/logo.png'))
        self.setWindowTitle(name)
        self.menuBar()
        self.widget = QTextEdit(self)
        #self.widget = Dessin()
        self.setCentralWidget(self.widget)

    def menuBar(self):
        super().statusBar()
        bar = super().menuBar()
        fileMenu = bar.addMenu("Fichier")
        fileToolBar = QToolBar("Fichier")
        acts = []
        acts.append(self.act("Open",self.openFile))
        acts.append(self.act("Save",self.saveFile))
        acts.append(self.act("Copy",self.copyFile))
        acts.append(self.act("Quit",self.quit))
        for action in acts:
            fileMenu.addAction(action)
            fileToolBar.addAction(action)
        self.addToolBar(Qt.TopToolBarArea,fileToolBar)
        

    def act(self,name,action):
        theAct = QAction(QIcon("media/"+name[0].lower()+name[1:]+".png"),name+"...", self )
        theAct.setShortcut( "Ctrl+"+name[0] )
        theAct.setToolTip(name)
        theAct.setStatusTip(name)
        theAct.triggered.connect( action )
        return theAct

    def openFile(self,value):
        fileName = QFileDialog.getOpenFileName(self, "Open File", "./test", "Text Files (*.txt *.html)") 
        file = QFile(fileName[0])
        file.open(QFile.ReadOnly | QFile.Text)
        content = QTextStream(file).readAll()
        if fileName[0].split(".")[1] == "html":
            self.widget.setHtml(content)
        else:
            self.widget.setPlainText(content)

    def saveFile(self,value):
        try:
            fileName = QFileDialog.getSaveFileName(self, "Save File", "./test", "Text Files (*.txt *.html)")
            file = open(fileName[0],'w')
            text = self.widget.toPlainText()
            file.write(text)
            file.close()
        except:
            pass
    
    def copyFile(self,value):
        print("copy")

    def quit(self,value):
        self.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
