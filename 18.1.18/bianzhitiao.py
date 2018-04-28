#!usr/bin/python
#conding=utf-8
import tkinter
import tkinter.messagebox
import os
import tkinter.filedialog
import time
import threading
import pygame
import winsound
app=tkinter.Tk()
app.overriderredirect(True)
app['width']=800
app['height']=600
menu=tkinter.Menu(app)

submenu=tkinter.Menu(menu,tearoff=0)
def Memorandum():
    varContent=tkinter.StringVar()
    varContent=set('')
    labelContent=tkinter.Label(app,text='Memorandum:',justify=tkinter.RIGHT,width=80)
    labelContent.place(x=10,y=5,width=80,height=120)
    entryContent=tkinter.Entry(app,width=80,textvariable=varContent)
    entryContent.place(100,y=5,width=80,height=20)
    def wancheng():
        varContent=entryContent.get()
    buttonOk=tkinter.Button(app,text='Wancheng',command=wancheng)
    buttonOk.place(x=30,y=70,width=50,height=20)
    def cancel():
        varContent.set('')
    buttonCancel=tkinter.Button(app,text='Cancel',command=cancel)
    buttonCancel.place(x=90,y=70,width=50,height=20)
    app.mainloop()
submenu.add_command(label='Memo',command=Memorandum)
def Close():
    app.destroy()
submenu.add_command(label='Close',command=Close)
menu.add_cascade(label='File',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def add_friend():
    global result
    varName=tkinter.StringVar()
    varName.set('')
    varId=tkinter.StringVar()
    varId.set('')
    labelName=tkinter.Label(app,text='Name:',justify=tkinter.RIGHT,width=50)
    labelName.place(x=10,y=5,width=50,height=20)
    entryName=tkinter.Entry(app,width=120,textvariable=varName)
    entryName.place(x=70,y=5,width=120,height=20)
    labelId=tkinter.Label(app,text='Id:',justify=tkinter.RIGHT,width=50)
    labelId.place(x=10,y=5,width=50,height=20)
    entryId=tkinter.Entry(app,width=120,textvariable=varId)
    entryId.place(x=70,y=5,width=120,height=20)
    def addInformation():
        result=entryName.get()+entryId.get()
    buttonAdd=tkinter.Button(app,text='Add',width=40,command=addInformation)
    buttonAdd.place(x=130,y=100,width=40,height=20)
submenu.add_command(label='add_friend ',command=add_friend)
def friendlist():
    global result
    listboxFriends=tkinter.Listbox(app,width=300)
    listboxFriendsplace(x=10,y=130,width=300,height=200)
    def deleteSelection():
        selection=listboxFriends.curselection()
        if not selection:
            tkinter.messagebox.showinfo(title='Information',messge='NO Selection')
        else:
            listboxFriends.delete(selection)
    buttonDelete=tkinter.Button(app,text='DeleteSelection',width=100,command=deleteSelection)
    buttonDelete.place(x=180,y=100,width=100,height=20)
submenu.friendlist(label='friendlist',command=friendlist)
menu.add_cascade(label='message',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def play():
    folder=''
    musics=[folder+'\\'+music for music in os.listdir(folder)\
            if music.endwith(('.mp3','.wav','.ogg'))]
    total=len(musics)
    pygame.mixer.init()
    while palying:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(1)
            musicName.set('playing....'+nextmusic)
        else:
            time.sleep(0.3)
    def buttonPlayClick():
        if not folder:
            folder=tkinter.filedialog.askdirectory()
        if not folder:
            return
        global playing
        playing=True
        t=threading.Thread(target=play)
        t.start()
        buttonPlay['state']='disabled'
        buttonStop['state']='normal'
    buttonPlay=tkinter.Button(app,text='Play',command=buttonPlayClick)
    buttonPlay.place(x=20,y=10,width=50,height=20)
    def buttonStopClick():
        global playing
        playing=False
        pygame.mixer.music.stop()
        musicName.set('暂时未播放音乐')
        buttonPlay['state']='normal'
        buttonStop['state']='disabled'
    buttonStop=tkinter.Button(app,text='Stop',command=buttonStopClick)
    buttonStop.place(x=80,y=10,width=50,height=20)
submune.add_command(label='Play',command=Play)
def Click():
    my_hour=input('请输入小时')
    my_minute=input('请输入分钟')
    flag=1
    while flag:
        t=time.localtime()
        fmt='%H,%M'
        now=time.strftime(fmt,t)
        now=now.split(',')
        hour=now[0]
        minute=now[1]
        if hour==my_hour and minute==my_minute:
            music='good time.wav'
            tkinter.messagebox.showinfo(title='Click',message='Is time')
            winsound.PlaySound(music,winsound.SND_ALIAS)
            flag=0
submenu.add_command(label='Click',command=Click)
menu.add_cascode(label='Options',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def Size_color():
    pass
submenu.add_command(label='Size_color',command=Size_color)
menu.add_cascode(label='Windows',menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
def About():
    tkinter.messagebox.showinfo(title='About',message='Author:xu')
submenu.add_command(label='About',command=About)
menu.add_cascode(label='help',menu=submenu)
app.mainloop()
