# -*- coding:utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 6666
BUFFER_SIZE = 1024
sock.bind((UDP_IP,UDP_PORT))

while 1:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print data, addr




