# -*- coding:utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP

UDP_IP = "127.0.0.1"
UDP_PORT = 6666

count = 0
while 1:
    message = str(count)
    sock.sendto(message,(UDP_IP,UDP_PORT))#send message to server
    count += 1



