#!usr/bin/python
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os
import fnmatch
import tkinter.scrolledtext
def search():
    entkw = entKw.get()
    enttype = entType.get()
    if not (entkw and enttype):
        tkinter.messagebox.showerror('出错了','关键字和类型都不能为空')
        return
    path = tkinter.filedialog.askdirectory()
    fnlist = os.walk(path)
    listbox.delete(0,tkinter.END)
    for i,dirs,files in fnlist:
        for n in fnmatch.filter(files,enttype):
            fn = '%s/%s'%(i,n)
            fn = fn.replace('\\','/')
            f = open(fn,'r',encoding='utf-8')
            if entkw in f.read():
                listbox.insert(tkinter.END,fn)
            f.close()
def text(event):
    fn = listbox.get(listbox.curselection())
    str1 = open(fn,encoding='utf-8').read()
    editWindow = tkinter.Tk()
    editWindow.title(fn)
    editWindow.geometry('+100+100')
    editText = tkinter.scrolledtext(editWindow,width=500,height=400)
    editText.grid()
    editText.insert(INSERT,str1)
    editWindow.mainloop()
root = tkinter.Tk()
root.title('文件搜索工具')
root.geometry('+120+100')
tkinter.Label(root,text='关键字:').grid()
entKw = tkinter.Entry(root)
entKw.grid(row=0,column=1)
tkinter.Label(root,text='文件类型:').grid(row=0,column=2)
entType = tkinter.Entry(root)
entType.grid(row=0,column=3)
btn = tkinter.Button(root,text='搜索',command=search)
btn.grid(row=0,column=4)
listbox = tkinter.Listbox(root,width=55)
listbox.bind('<Double-Button-1>',text)
listbox.grid(row=1,columnspan=5)
root.mainloop()
