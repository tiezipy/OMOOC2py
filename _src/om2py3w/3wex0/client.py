# -*- coding:utf-8 -*-
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
server_addr = ('127.0.0.1',6666)


print '''    [h] for history
    [q] close server
    [ENTRE] close client
    write your daily now...    '''

while 1:
    message = raw_input('>>')#输入q关闭服务器
    client.sendto(message, server_addr)
    if message == '':#退出while关闭client
        break
    elif message == 'h':
        daily = open('socket_daily.log')
        print '*'*10,'history','*'*10
        print daily.read()
        print '*'*10,'history','*'*10

client.close()






