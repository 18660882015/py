#!usr/bin/python
#conding=utf-8
def buttonZuoyeClick():
    xuehao=entryXuehao.get()
    xingming=entryXingming.get()
    serverIP=entryServerIP.get()
    if not re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',serverIP):
        tkinter.messagebox.showerror('很抱歉','服务器IP地址不合法')
        return
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((serverIP,30300))
    except Exception as e:
        tkinter.messagebox.showerror('很抱歉','现在不是交作业时间')
        return
    filename=xuehao+'_'+xingming+'.png'
    im=ImageGrab.grab()
    im.save(filename)
    im.close()
    BUFSIZE=1024
    FILEINFO_SIZE=struct.calcsize('I128sI')
    fhead=struct.pack('I128sI',len(filename),filename.encode(),os.stat(filename).st_size)
    sock.send(fhead)
    data=sock.recv(1024)
    data=data.decove()
    if data.lower()=='notmatch':
        tkinter.messagebox.showerror('很抱歉','学号与姓名不匹配')
        sock.close()
        return
    fp=open(filename,'rb')
    while True:
        filedata=fp.read(BUFSIZE)
        if not filedata:
            break
        sock.send(filedata)
    fp.close()
    sock.close()
    tkinter.messagebox.showinfo('恭喜','交作业成功')
buttonZuoye=tkinter.Button(root,text='全屏截图交作业',command=buttonZuoyeClick)
buttonZuoye.place(x=120,y=90,width=100,height=20)
