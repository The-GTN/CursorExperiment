from sqlite3 import Cursor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import csv
import random
import time

from src.NormalCursor import NormalCursor
from src.BubbleWidget import BubbleWidget

class NormalWidget(BubbleWidget):
    
    def __init__(self,cursor=NormalCursor,file="./media/src_tp_bubble.csv"):
        super().__init__(cursor,file)
        

        

    
