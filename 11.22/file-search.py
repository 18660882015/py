#!usr/bin/python
#conding=utf-8
from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import fnmatch
from ScrolledText import ScrolledText
def search():
    entkw = entKw.get()
    if not (entkw and enttype):
        tkMessageBox.showerror('出错了','关键字和类型都不能为空')
        return
    path = tkFileDialog.askdirectory()
    fnlist = os.walk(path)
    listbox.delete(0,END)
    for i,dirs,files in fulist:
        fn = '%s/%s'%(i,n)
        fn = fn.replace('\\','/')
        f = open(fn)
        if entkw in f.read():
            litsbox.insert(END,fn)
        f.close()
def text(event):
    fn = listbox.get(listbox.curselection())
    str1 = open(fn).read()
    editWindow = Tk()
    editWindow.title(fn)
    editWindow.geometry('+2000+150')
    editText = ScrolledText(editWindow,width=120,height=60)
    editText.grid()
    editText.insert(INSERT,str1)
    editWindow.mainloop()
root = Tk()
root.title('文件搜索工具')
root.geometry('+2400+300')
Label(root,text='关键字:').grid()
entKw = Entry(root)
entKw.grid(row=0,column=1)
Label(root,text='文件类型:').grid(row=0,column=2)
entType = Entry(root)
entType.grid(row=0,column=3)
btn = Button(root,text='搜索',command=search)
btn.grid(row=0,column=4)
listbox = Listbox(root,width=80)
listbox.bind('<Double-Button-1>',text)
listbox.grid(row=1,column=5)
root.mainloop()
