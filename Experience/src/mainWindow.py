from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.Experience.ExpSetup import ExpSetup
from src.Experience.XPManager import XPManager

class MainWindow(QMainWindow):

    def __init__(self,name="Expérience contrôlée"):
        super().__init__()
        self.setWindowIcon(QIcon('media/images/logo.png'))
        self.setWindowTitle(name)
        self.setWidget(QWidget)
        self.err = False
        self.manager = None
        ExpSetup(self)

    def setWidget(self,widget,opts={}):
        if len(opts) == 0:
            self.widget = widget()
        else:
            self.manager = XPManager(self,opts)
            self.widget = self.manager.setWidget(widget)
        self.setCentralWidget(self.widget)

    def closeEvent(self, event):
        if self.err:
            event.accept()
        else:
            reply = QMessageBox.question(self, 'Stop Experience', 'Are you sure you want to stop the experiment ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def error(self):
        self.err = True
        self.close()