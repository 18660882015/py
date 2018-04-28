#!usr/bin/python
#conding=utf-8
class windowKaoshi:
    def __init__(self,root,conn,xuehaoxingming):
        self.top=tkinter.Toplevel(root,width=300,height=220)
        self.top.title('学生自测———'+xuehaoxingming)
        self.top.attributes('-topmost',1)
        self.top.resizable(False,False)
        def closeWindow():
            if int_windowZice.get()==1:
                int_windowZice.set(0)
                conn.sendall('xxxx'.encode())
                conn.close()
            self.top.destroy()
        self.top.protocol('WM_DELETE_WINDOW',closeWindow)
        data=conn.recv(1024)
        data=data.decode()
        kechengQingdan=data.split(',')
        labelKechengmingcheng=tkinter.Label(self.top,text='请选择课程名称:')
        labelKechengmingcheng.place(x=10,y=10,height=20,width=100)
        comboboxKechengmingcheng=tkinter.ttk.Combobox(self.top,values=kechengqingdan)
        comboboxKechengmingcheng.place(x=120,y=10,height=20,width=130)
        def comboxboxKechengmingChanged(event):
            self.currentID=10
        comboboxKechengmingcheng.bind('<<ComboboxSelected>>',comboxboxKechengmingchanged)
        string_Kecheng=tkinter.StringVar(self.top,value='')
        labelKecheng=tkinter.Label(self.top,text='',textvariable=string_Kecheng)
        labelKecheng.place(x=10,y=40,height=20,width=100)
        entryMessage=tkinter.scrolledtext.ScrolledText(self.top,wrap=tkinter.WORD)
        entryMessage.place(x=10,y=70,width=280,height=70)
        def buttonNextClick():
            kechengmingchengSelected=comboboxKechengmingcheng.get()
            if not kechengmingchengSelected:
                tkinter.messagebox.showerror('很抱歉','请选择课程名称')
                return
            if entryMessage.get(0.0).strip()!=''and entryDaan.get().strip()=='':
                tkinter.messagebox.showinfo('很抱歉','必须做这个题')
                return
            if len(entryDaan.get())>=200:
                tkinter.messagebox.showerror('很抱歉','答案太长了')
                return
            message=(kechengmingchengSelected+'xx'+str(self.currentID)+'xx'+entryDaan.get()+'xxnext')
            conn.sendall(message.encode())
            data=connrecv(1024)
            data=data.decode()
            if data.startswith('no,'):
                fenshu=data.split(',')[1]
                tkinter.messagebox.showinfo(title='恭喜',message='得分:'+fenshu)
                buttonNext['state']='disabled'
                return
            kechengmingcheng,zhangjie,timu,self.currentID=data.split('xx')
            entryMessage.delete(0.0,tkinter,END)
            entryMessage.insert(tkinter.INSERT,timu)
            string_Kecheng.set(kechengmingcheng)
            entryDaan.delete(0,tkinter.END)
            buttonNext=tkinter.Button(self.top,text='下一题',command=buttonNextClick)
            buttonNext.place(x=10,y=150,width=60,height=20)
            entryDaan=tkinter.Entry(self.top,)
            entryDaan.place(x=10,y=180,width=270,height=20)
            buttonNextClick()
