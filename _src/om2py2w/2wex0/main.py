#-*- coding:utf-8 -*-

from Tkinter import *
import time
from os.path import exists

daily_file = "daily.txt"

def main():

	root = Tk()
	root.title("我的日记本") #窗口的标题
	root.geometry("600x400+50+50") #600x400是初始化窗口的大小，0，0是窗口的初始位置


	def ShowHistory():
		if exists(daily_file):
			daily = open(daily_file,'r')
			T.delete(1.0,END) #删除text窗口中之前显示的内容 
			T.insert(END,"="*18+'\n')
			T.insert(END,daily.read())
			T.insert(END,"="*18+'\n')
			daily.close()
		else:
			T.insert(END,"对不起你还没开始写日记.\n")

	def ClearDaily():
		if exists(daily_file):
			daily = open(daily_file,"w")
			T.delete(1.0,END)
			T.insert(END,"已删除日记 \n")
			daily.close()
		else:
			T.insert(END, "对不起你还没开始写日记.\n")

	def AddLine(event):
		daily = open(daily_file,"a")
		new_line = E.get().encode('utf-8')
		current_time = time.strftime("<%Y-%m-%d %H:%M:%S>")
		daily.write(current_time+'\t')
		daily.write(new_line +'\n')
		daily.close()
		E.delete(0,END)

		T.insert(END,new_line)

	frm = Frame(root,height = 5)
	frm.pack()

	button1 = Button(frm,text = "历史记录",width =20,command = ShowHistory)
	button1.pack(side ='left',padx =5, pady = 2)

	button2 = Button(frm, text = "清除记录",width = 20, command = ClearDaily)
	button2.pack(side ='left',padx = 5, pady = 2)

	button3 = Button(frm, text = "关闭日记", width = 20, command = root.destroy)
	button3.pack(side ='left',padx = 5, pady = 2)

	T = Text(root,height= 25,bg = "grey", font = "Aral 10")
	T.pack()

	frm2 = Frame(root, height = 10)
	frm2.pack()

	L = Label(frm2,text = "这里输入")
	L.pack(side = 'left', padx = 0)

	E = Entry(frm2, text = ">>",width = 35)
	E.pack(side = 'left')
	E.bind("<Return>",AddLine)

	root.mainloop()

if __name__ == "__main__":
	main()


