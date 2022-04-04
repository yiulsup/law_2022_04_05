from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ethernet import *
import numpy
import sys
import queue
from struct import *
from protocol import *
import time

class management_system(QMainWindow):
    def __init__(self):
        super(management_system, self).__init__()
        uic.loadUi("./UI/management_system.ui", self)
        self.show()

        self.aliveQueue = queue.Queue()
        self.acq_dataQueue = queue.Queue()

        self.pHome.setStyleSheet("border:none;")
        self.pCell.setStyleSheet("border:none;")
        self.pDevice.setStyleSheet("border:none;")
        self.pUser.setStyleSheet("border:none;")
        self.sWidget.setCurrentIndex(0)

        self.pHome.clicked.connect(self.home)
        self.pCell.clicked.connect(self.cell)
        self.pDevice.clicked.connect(self.device)
        self.pUser.clicked.connect(self.user)

        self.eth = ethernet(self)
        self.eth.start()

        self.timerClock = QTimer(self)
        self.timerClock.setInterval(1000)
        self.timerClock.timeout.connect(self.clock)
        self.timerClock.start()

        #self.alive_thread = alive(self)
        #self.alive_thread.start()

        self.timerMutex = QMutex()
        self.styleMutex = QMutex()
        self.mutexalive = QMutex()

    @pyqtSlot(int)
    def stySheet(self, value):
        udata = self.aliveQueue.get()
        self.mutexalive.lock()
        self.sdata = unpack(STRUCT_CID_ALIVE_REP, udata)
        self.ID = self.sdata[2].decode('utf-8')
        self.intID = int(self.ID)
        if self.intID == 0x1:
            if self.sdata[3] == 1:
                self.n1_mainsys.setStyleSheet('background-color:#0000ff')

            else:
                self.n1_mainsys.setStyleSheet('background-color:#ff0000')

            if self.sdata[4] == 1:
                self.n1_mainradar.setStyleSheet('background-color:#0000ff')

            else:
                self.n1_mainradar.setStyleSheet('background-color:#ff0000')

            if self.sdata[5] == 1:
                self.n1_subsys.setStyleSheet('background-color:#0000ff')

            else:
                self.n1_subsys.setStyleSheet('background-color:#ff0000')

            if self.sdata[6] == 1:
                self.n1_subradar.setStyleSheet('background-color:#0000ff')

            else:
                self.n1_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x2:
            if self.sdata[3] == 1:
                self.n2_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n2_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n2_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n2_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n2_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n2_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n2_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n2_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x3:
            if self.sdata[3] == 1:
                self.n3_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n3_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n3_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n3_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n3_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n3_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n3_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n3_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x4:
            if self.sdata[3] == 1:
                self.n4_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n4_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n4_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n4_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n4_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n4_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n4_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n4_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x5:
            if self.sdata[3] == 1:
                self.n5_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n5_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n5_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n5_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n5_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n5_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n5_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n5_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x6:
            if self.sdata[3] == 1:
                self.n6_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n6_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n6_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n6_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n6_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n6_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n6_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n6_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x7:
            if self.sdata[3] == 1:
                self.n7_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n7_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n7_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n7_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n7_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n7_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n7_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n7_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x8:
            if self.sdata[3] == 1:
                self.n8_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n8_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n8_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n8_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n8_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n8_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n8_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n8_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 0x9:
            if self.sdata[3] == 1:
                self.n9_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n9_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n9_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n9_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n9_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n9_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n9_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n9_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 10:
            if self.sdata[3] == 1:
                self.n10_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n10_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n10_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n10_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n10_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n10_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n10_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n10_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 11:
            if self.sdata[3] == 1:
                self.n11_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n11_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n11_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n11_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n11_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n11_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n11_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n11_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 12:
            if self.sdata[3] == 1:
                self.n12_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n12_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n12_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n12_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n12_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n12_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n12_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n12_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 13:
            if self.sdata[3] == 1:
                self.n13_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n13_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n13_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n13_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n13_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n13_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n13_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n13_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 14:
            if self.sdata[3] == 1:
                self.n14_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n14_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n14_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n14_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n14_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n14_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n14_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n14_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 15:
            if self.sdata[3] == 1:
                self.n15_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n15_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n15_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n15_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n15_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n15_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n15_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n15_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 16:
            if self.sdata[3] == 1:
                self.n16_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n16_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n16_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n16_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n16_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n16_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n16_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n16_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 17:
            if self.sdata[3] == 1:
                self.n17_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n17_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n17_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n17_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n17_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n17_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n17_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n17_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 18:
            if self.sdata[3] == 1:
                self.n18_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n18_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n18_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n18_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n18_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n18_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n18_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n18_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 19:
            if self.sdata[3] == 1:
                self.n19_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n19_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n19_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n19_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n19_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n19_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n19_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n19_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 20:
            if self.sdata[3] == 1:
                self.n20_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n20_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n20_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n20_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n20_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n20_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n20_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n20_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 21:
            if self.sdata[3] == 1:
                self.n21_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n21_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n21_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n21_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n21_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n21_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n21_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n21_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 22:
            if self.sdata[3] == 1:
                self.n22_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n22_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n22_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n22_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n22_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n22_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n22_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n22_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 23:
            if self.sdata[3] == 1:
                self.n23_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n23_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n23_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n23_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n23_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n23_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n23_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n23_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 24:
            if self.sdata[3] == 1:
                self.n24_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n24_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n24_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n24_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n24_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n24_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n24_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n24_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 25:
            if self.sdata[3] == 1:
                self.n25_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n25_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n25_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n25_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n25_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n25_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n25_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n25_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 26:
            if self.sdata[3] == 1:
                self.n26_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n26_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n26_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n26_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n26_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n26_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n26_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n26_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 27:
            if self.sdata[3] == 1:
                self.n27_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n27_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n27_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n27_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n27_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n27_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n27_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n27_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 28:
            if self.sdata[3] == 1:
                self.n28_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n28_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n28_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n28_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n28_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n28_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n28_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n28_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 29:
            if self.sdata[3] == 1:
                self.n29_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n29_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n29_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n29_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n29_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n29_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n29_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n29_subradar.setStyleSheet('background-color:#ff0000')
        elif self.intID == 30:
            if self.sdata[3] == 1:
                self.n30_mainsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n30_mainsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[4] == 1:
                self.n30_mainradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n30_mainradar.setStyleSheet('background-color:#ff0000')
            if self.sdata[5] == 1:
                self.n30_subsys.setStyleSheet('background-color:#0000ff')
            else:
                self.n30_subsys.setStyleSheet('background-color:#ff0000')
            if self.sdata[6] == 1:
                self.n30_subradar.setStyleSheet('background-color:#0000ff')
            else:
                self.n30_subradar.setStyleSheet('background-color:#ff0000')
        self.mutexalive.unlock()

    def clock(self):
        self.timerMutex.lock()
        self.nowDate = QDate.currentDate()
        self.nowTime = QTime.currentTime()
        self.date.setText(self.nowDate.toString(Qt.DefaultLocaleLongDate))
        self.time.setText(self.nowTime.toString(Qt.DefaultLocaleLongDate))
        self.timerMutex.unlock()


    def home(self):
        self.sWidget.setCurrentIndex(0)

    def cell(self):
        self.sWidget.setCurrentIndex(1)

    def device(self):
        self.sWidget.setCurrentIndex(2)

    def user(self):
        self.sWidget.setCurrentIndex(3)

app = QApplication(sys.argv)
window = management_system()
window.show()
app.exec_()
