import socket
from PyQt5.QtCore import *
from define import *
import queue
import numpy as np
import asyncio

class eth_recv(QThread):
    image_signal = pyqtSignal(int)
    def __init__(self, parent, conn, eth):
        super(eth_recv, self).__init__()
        self.parent = parent
        self.conn = conn
        self.eth = eth
        self.eth_recv_mutex = QMutex()

    @pyqtSlot()
    def run(self):
        while True:

            self.raw = self.conn.recv(1024)
            self.eth_recv_mutex.lock()
            if self.raw == b'':
                break

            if self.raw[0] == 0x4 and self.raw[1] == 0x01:
                self.parent.aliveQueue.put(self.raw)
                self.image_signal.emit(1)

            elif self.raw[0] == 0x04 and self.raw[1] == 0x11:
                self.parent.acq_dataQueue.put(self.raw)
            self.eth_recv_mutex.unlock()

        self.eth_recv_mutex.unlock()
        print("Thread Quit")
        self.quit()

    def stop(self):
        self.quit()
        self.wait(3000)



class ethernet(QThread):
    def __init__(self, parent):
        super(ethernet, self).__init__()
        self.parent = parent
        self.eth = QMutex()

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind((IP, PORT))
        self.sock.listen(50)
        print("Listen")
        self.cnt = 1
        while True:
            self.conn, addr = self.sock.accept()
            print("Connected")
            self.eth.lock()
            self.eth_thread_recv = eth_recv(self.parent, self.conn, self)
            self.eth_thread_recv.image_signal.connect(self.parent.stySheet)
            self.eth_thread_recv.start()
            self.eth.unlock()
