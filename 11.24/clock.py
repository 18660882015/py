#!usr/bin/python
import tkinter
import tkinter.messagebox
import time
import os
def yes():
    root.attributes('-alpha',0.1)
    root.attributes('-topmost',0)
    enth = entH.get()
    entm = entM.get()
    flag=1
    while flag:
        t = time.localtime(time.time())
        fmt = '%H %M'
        now = time.strftime(fmt,t)
        now = now.split(' ')
        hour = now[0]
        minute = now[1]
        if hour == enth and minute == entm:
            tkinter.messagebox.showerror('时间到','您定的时间到了')
            flag = 0
            root.attributes('-alpha',1)
root = tkinter.Tk()
root.title('桌面闹钟')
root.geometry('+0+0')
tkinter.Label(root,text='时:').grid()
entH = tkinter.Entry(root)
entH.grid(row=0,column=1)
tkinter.Label(root,text='分:').grid(row=0,column=2)
entM = tkinter.Entry(root)
entM.grid(row=0,column=3)
btn = tkinter.Button(root,text='确定',command=yes)
btn.grid(row=0,column=4)
root.mainloop()
