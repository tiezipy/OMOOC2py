# -*- coding:utf-8 -*-
#---server---
import socket
import time

server = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM) #UDP
server_addr = ('127.0.0.1', 6666)
size = 1024
server.bind(server_addr)

while 1: #服务端保持一直接收信息
    data, addr = server.recvfrom(size)
    if data == 'q':#接收到client端q指令退出while关闭服务器
        print 'quit...'
        break
    elif data == 'h':
        daily = open('socket_daily.log','r').read()
        server.sendto(daily, addr)
    elif data == '':
        print "nothing, client is closing..."
    else:
        print 'data:', data, 'from',addr, 'save to socket_daily.log ...'
        daily = open("socket_daily.log", 'a+')
        current_time = time.strftime('[%Y-%m-%d %H:%M:%S]')
        daily.write(current_time +' '+ data +'\n')
        daily.close()

server.close()




