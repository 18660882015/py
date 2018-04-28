#!usr/bin/python
#conding=utf-8
import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext
app=tkinter.Tk()
app.title('My notepad---by xu')
app['width']=800
app['height']=600
textChanged=tkinter.IntVar(value=0)
filename=''
menu=tkinter.Menu(app)
submenu=tkinter.Menu(app)
submenu=tkinter.Menu(menu,tearoff=0)
def Open():
    global filename
    if textChanged.get():
        yesno=tkinter.messagebox.askyesno(title='Save or not?',message='Do you want to save?')
        if yesno ==tkinter.YES:
            Save()
    filename=tkinter.filedialog.askopenfilename(title='Open file',filetypes=[('Text files','*.text')])
    if filename:
        textContent.delete(0.0,tkinter.END)
        fp=open(filename,'r')
        textContent.insert(tkinter.INSERT,''.join(fp.readlines()))
        fp.close()
        textChanged.set(0)
submenu.add_command(label='Open',command=Open)
def Save():
    global filename
    if not filename:
        SaveAs()
    elif textChanged.get():
        fp=open(filename,'w')
        fp.write(textContent.get(0.0,tkinter.END))
        fp.close()
        textChanged.set(0)
submenu.add_command(label='Save',command=Save)
def SaveAs():
    global filename
    newfilename=tkinter.filedialog.asksaveasfilename(title='Save As',initiadir=r'c:\\',initiafile='new.text')
    if newfilename:
        fp=open(newfilename,'w')
        fp.write(textContent.get(0.0,tkinter.END))
        fp.close()
        filename=newfilename
        textChanged.set(0)
submenu.add_command(label='Save As',command=SaveAs)
submenu.add_separator()
def Close():
    global filename
    Save()
    textContent.delete(0.0,tkinter.END)
    filename=''
submenu.add_command(label='Close',command=Close)
menu.add_cascade(label='File',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def Undo():
    textContnt['undo']=True
    try:
        textContent.edit_undo()
    except Exception as e:
        pass
submenu.add_command(label='Undo',command=Undo)
def Redo():
    textContent['undo']=True
    try:
        textContent.edit_redo()
    except Exception as e:
        pass
submenu.add_command(label='Redo',command=Redo)
submenu.add_separator()
def Copy():
    textContent.clipboard_clear()
    textContent.clipboard_append(textContent.selection_get())
submenu.add_command(label='Copy',command=Copy)
def Cut():
    copy()
    textContent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
submenu.add_command(label='Cut',command=Cut)
def Paste():
    try:
        textContent.insert(tkinter.SEL_FIRST,textContent.clioboard_get())
        textComtent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
        return
    except Exception as e:
        pass
    textContent.insert(tkinter.INSERT,textContent.clipboard_get())
submenu.add_command(label='Paste',command=Paste)
submenu.add_separator()
def Search():
    textToSearch=tkinter.simpledialog.askstring(title='search',prompt='What to search?')
    start=txtContent.search(textToSearch,0.0,tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title='Found',message='ok')
submenu.add_command(label='Search',command=Search)
menu.add_cascade(label='Edit',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def About():
    tkinter.messagebox.showinfo(title='About',message='Author:xu')
submenu.add_command(label='About',command=About)
menu.add_cascade(label='Help',menu=submenu)
app.config(menu=menu)
textContent=tkinter.scrolledtext.scrolledText(app,wrap=tkinter.WORD)
textContent.pack(fill=tkinter.BOTH,expand=tkinter.YES)
def KeyPress(event):
    textchanged.set(1)
textContent.bind('<KeyPress>',KeyPress)
app.mainloop()
