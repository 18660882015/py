#!usr/bin/python
#conding=utf-8
def buttonOKClick():
    xuehao=entryXuehao.get()
    xingming=entryXingming.get()
    serverIP=entryServerIP.get()
    if not re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',serverIP):
        tkinter.messagebox.showerror('很抱歉','服务器ip地址不合法')
        return
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((serverIP,30300))
    except:
        tkinter.messagebox.showerror('很抱歉','现在不是点名时间')
        return
    sock.sendall((xuehao+','+xingming).encode())
    data=sock.recv(1024)
    data=data.decode()
    if data.lower()=='ok':
        tkinter.messagebox.showinfo('恭喜',xuehao+','+xingming+'  报到点名成功')
        sock.close()
        return
    elif data.lower()=='repeat':
        tkinter.messagebox.showerror('很抱歉','不允许重复报到')
        sock.close()
        return
    elif data.lower()=='notmatch':
        tkinter.messagebox.showerror('很抱歉','学号与姓名不匹配')
        sock.close()
        return
    elif data.lower()=='daidianming':
        tkinter.messagebox.showerror('很抱歉','不允许替别人点名，警告一次')
        sock.close()
        return
buttonOk=tkinter.Button(root,text='报到',command=buttonOKClick)
buttonOk.place(x=30,y=90,width=80,height=20)
