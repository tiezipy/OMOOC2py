# -*- coding:utf-8 -*-
from sys import *
from os.path import exists


def main():
	print u"欢迎来到你的日记：1.打印历史记录 2.写入新内容  3.不写了，退出"
	choose = raw_input('>> ')
	if choose == '1':
		print_history()
	elif choose == '2':
		write_your_note()
	elif choose == '3':
		exit(0)
	else:
		print u"老兄你几个意思？"
		mai()


def print_history():

	if exists("daily.txt") :
		print u"这是你之前的记录："
		print 30 * '='
		filename = open("daily.txt",'r')
		for line in filename.readlines():
			print line
		print 30 * '='
		
	else:
		print u"你还没有写过日记！现在开始写吧！"
		filename = open("daily.txt",'w')
		filename.close()
		write_your_note()

def write_your_note():
	print u"请输入你的内容",
	lines = raw_input(">> ")
	filename = open("daily.txt",'a+')
	filename.write(lines + "\n")
	filename.close()
	


if __name__ == '__main__':
	main()
	










	






