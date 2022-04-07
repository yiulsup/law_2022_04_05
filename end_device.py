import socket
import threading
from struct import *
from queue import *
import time

def response(sock):
    while True:
        data = sock.recv(1024)
        if data[0] == 0x1 and data[1] == 0x1:
            data_alive_res = pack("HH12sBBBBI", 0x102, 16, "0".encode('utf-8'), 1, 1, 1, 1, 0)
            sock.send(data_alive_res)
        elif data[0] == 0x1 and data[1] == 0x2:
            data_get_boardinfo_res = pack("HH12s16sI16s16s32s16s16s16sB20BI",
                                          0x202, 148, "0".encode('utf-8'), "192.168.0.18".encode('utf-8'), 5600, "255.255.255.0".encode('utf-8'),
                                          "192.168.0.1".encode('utf-8'), "9810:6b7e:b2c2:2439".encode('utf-8'), "1.0".encode('utf-8'), "1.0".encode('utf-8'),
                                          "192.168.0.193".encode('utf-8'), 1,
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          32)
            sock.send(data_get_boardinfo_res)
        elif data[0] == 0x1 and data[1] == 0x4:
            data_set_boardinfo_res = pack("HH12s3BBI",
                                          0x402, 148, "0".encode('utf-8'),
                                          0, 0, 0, 0, 32)
            sock.send(data_set_boardinfo_res)
        elif data[0] == 0x1 and data[1] == 0x8:
            data_get_profileinfo_res = pack("HH12s32s HHHHHHHHHHHH fffIIff8BI",
                                            0x802, 48, "0".encode('utf-8'), "device_0_Profile".encode('utf-8'),
                                            1, 0, 1, 1, 456, 456, 5, 3, 2, 1, 7, 5, 3.4, 6.2, 0.00016, 14, 2, 1.15,
                                            0.0015, 0, 0, 0, 0, 0, 0, 0, 0, 32)
            sock.send(data_get_profileinfo_res)
        elif data[0] == 0x1 and data[1] == 0x10:
            data_set_profileinfo_res = pack("HH12s3BBI",
                                            0x1002, 16, "0".encode('utf-8'),
                                            0, 0, 0, 0, 32)
            sock.send(data_set_profileinfo_res)
        elif data[0] == 0x1 and data[1] == 0x14:
            data_reset_res = pack("HH12sB2BBI", 0x1402, 16, "0".encode('utf-8'), 8, 0, 0, 0, 32)
            sock.send(data_reset_res)


def alive_rep(sock):
    cnt = 0
    while True:
        #data_alive_res = pack("HH12sBBBBI", (0x102, 16, "0".encode('utf-8'), 1, 0, 1, 0, 0))
        data_alive_rep_0 = pack("HH12sBBBBI", 0x104, 16, "0".encode('utf-8'), 0, 0, 0, 0, 0)
        data_alive_rep_1 = pack("HH12sBBBBI", 0x104, 16, "0".encode('utf-8'), 1, 0, 0, 0, 0)
        data_alive_rep_2 = pack("HH12sBBBBI", 0x104, 16, "0".encode('utf-8'), 1, 1, 0, 0, 0)
        data_alive_rep_3 = pack("HH12sBBBBI", 0x104, 16, "0".encode('utf-8'), 1, 1, 1, 0, 0)
        data_alive_rep_4 = pack("HH12sBBBBI", 0x104, 16, "0".encode('utf-8'), 1, 1, 1, 1, 0)

        if cnt == 0:
            sock.send(data_alive_rep_0)
        elif cnt == 1:
            sock.send(data_alive_rep_1)
        elif cnt == 2:
            sock.send(data_alive_rep_2)
        elif cnt == 3:
            sock.send(data_alive_rep_3)
        elif cnt == 4:
            sock.send(data_alive_rep_4)
        time.sleep(30)
        cnt = cnt + 1
        if cnt == 5:
            cnt = 0

def acq_data(sock):
    while True:
        data_acq_data_rep = pack("HH12sBBBB3BBBBHHHBBHHHBBHHHHHHH36BI",
                                 0x1104, 64, "0".encode("utf-8"),
                                 0, 0, 0, 1, 0, 0, 0, 70, 1, 1, 200, 80, 15,
                                 1, 1, 150, 81, 19,
                                 1, 1, 153, 80, 17,
                                 1, 23, 43, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 32)
        sock.send(data_acq_data_rep)
        time.sleep(2)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5600))

t1 = threading.Thread(target=response, args=(sock, ))
t1.start()

t2 = threading.Thread(target=alive_rep, args=(sock, ))
t2.start()

t3 = threading.Thread(target=acq_data, args=(sock, ))
t3.start()

while True:
    pass


