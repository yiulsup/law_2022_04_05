import sqlite3
import pandas as pd
import cv2
import numpy as np
import sys
import socket
import time
import datetime
import sqlite3
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QImage, QPixmap
import query
import protocol
from struct import *

class database(QThread):
    def __init__(self, parent, flex_recv_parser):
        super(database, self).__init__()
        self.flex_recv_parser = flex_recv_parser
        self.parent = parent
    def run(self):
        self.conn = sqlite3.connect("dbTest.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE alive")
        self.conn.commit()
        self.cur.execute("DROP TABLE acq_data")
        self.conn.commit()
        self.conn = sqlite3.connect("dbTest.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(query.sql_alive_create)
        self.conn.commit()
        self.cur.execute(query.sql_acq_data_create)
        self.conn.commit()

        while True: pass
