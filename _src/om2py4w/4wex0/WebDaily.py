#-*- coding:utf-8 -*-
from bottle import *
import sys
import time

def ReadDaily():
	f = open('myDaily.txt','r')
	return f.read()

def WriteDaily(NewDaily):
	f = open('myDaily.txt','a+')
	write_time = time.strftime('[%Y/%m/%d %H:%S:%M] ')
	f.write(write_time + NewDaily + '\n')
	f.close()

@route('/daily')
def HistoryDaily():
	daily = ReadDaily()
	return template('myDaily.tpl',message = daily)

@route('/daily',method = 'POST')
def NewDaily():
	NewDaily = request.forms.get('NewDaily')
	WriteDaily(NewDaily)
	newmsg = ReadDaily()
	return template('myDaily.tpl', message = newmsg)


if __name__ == '__main__':
	run(host = 'localhost', port = 8080,debug = True, reloader = 1)