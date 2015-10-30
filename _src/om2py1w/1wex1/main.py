# -*- coding:utf-8 -*-
from sys import *
from os.path import exists
import time

def main():
	print_history()
	write_your_note()
	
def print_history():
	#打印历史记录
	if exists("daily.txt") :  #判断是否是第一次写日记
		print 50 * '*'
		daily = open("daily.txt",'r')
		for line in daily.readlines(): #读取方式
			print line
		print 50 * '*'
		print u"以上是历史记录，请在'>>'后输入新内容"
	else:
		print u'你的日记还没有记录,请在提示符后输入内容，ENTER直接退出！'
		write_your_note()
	
def write_your_note():
	#写入日记内容
    lines = raw_input(">> ")
    if lines== '': #若没有输入任何内容，直接enter退出
		exit(0)
    else:
		daily = open("daily.txt",'a+')
		daily.write(write_time() + ' ')
		daily.write(lines + '\n')
		daily.close()
		main()

def write_time():
	#日记输入时间
    time_format = '<%Y-%m-%d %H:%M:%S>'
    return time.strftime(time_format)

if __name__ == '__main__':
	main()
	










	






