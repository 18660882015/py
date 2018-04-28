#!usr/bin/python
#conding=utf-8
class windowsChakanXueshengXinxi:
    def __init__(self,root,myTitle):
        self.top=tkinter.Toplevel(root,width=350,height=400)
        self.top.title(myTitle)
        self.top.attributes('-topmost',1)
        xueshengZhuanye=Common.getZhuanye()
        comboboxZhuanye=tkinter.ttk.Combobox(self.top,values=xueshengZhuanye)
        comboboxZhuanye.place(x=20,y=20,height=20,width=100)
        def buttonChakanClick():
            zhuanye=comboboxZhuanye.get()
            if not zhuanye:
                tkinter.messagebox.showerror(title='抱歉',message='请选择专业')
                return
            temp=Common.getXuehaoXingming(zhuanye)
            for row in treeXueshengMingdan.get_children():
                treeXueshengMingdan.delete(row)
            iii=0
            for student in temp:
                student=student.split(',')
                treeXueshengMingdan.insert('',iii,values=(student[0],student[1]))
                iii=iii+1
        self.frame=tkinter.Frame(self.top)
        self.frame.place(x=20,y=50,width=200,height=280)
        scrollBar=tkinter.Scrollbar(self.frame)
        scrollBar=pack(side=tkinter.RIGHT,fill=tkinter.Y)
        treeXueshengMingdan=tkinter.ttk.Treeview(self.frame,columns=('col1','col2'),show="headings",yscrollcommand=scrollBar.set)
        treeXueshengMingdan.column('col1',width=90,anchor='center')
        treeXueshengMingdan.column('col2',width=90,anchor='center')
        treeXueshengMingdan.heading('col1',text='学号')
        treeXueshengMingdan.heading('col2',text='姓名')
        def onDBClick(event):
            if not treeXueshengMingdan.selection():
                tkinter.messagebox.showerror('很抱歉','请选择学生')
                return
            item=treeXueshengMingdan.selection()[0]
            xuehaoDianming=treeXueshengMingdan.item(item,'values')[0]
            xingmingDianming=treeXueshengMingdan.item(item,'values')[1]
            currentTime=Common.getCurrentDateTime()
            startTime=Common.getStartDateTime()
            sqlShifouChongfuDianming="SELECT count(xuehao)FROM dianming WHERE xuehao='"+xuehaoDianming+"'AND shijian >='"+startTime+"'"
            if Common.getDataBySQL(sqlShifouChongfuDianming)[0][0]!=0:
                tkinter.messagebox.showerror('很抱歉',xueshengDianming+','+xingmingDianming+'重复点名')
                return
            sqlDianming="INSERT INTO dianming(xuehao,shijian)VALUES('"+xuehaoDianming+"','"+currentTime+"')"
            Common.doSQL(sqlDianming)
            tkinter.messagebox.showinfo('恭喜',xuehaoDianming+','+xingmingDianming+'点名成功')
        treeXueshengMingdan.bind("<Double-1>",onDBClick)
        treeXueshengMingdan.pack(side=tkinter.LEFT,fill=tkinter.Y)
        scrollBar.config(command=treeXueshengMingdan.yview)
        buttonChakan=tkinter.Button(self.top,text='查看',command=buttonChakanClick)
        buttonChakan.place(x=130,y=20,height=20,width=40)
        def buttonJiafenClick():
            if nottreeXueshengMingdan.selection():
                tkinter.messagebox.showerror('很抱歉','请选择学生')
                return
            item=treeXueshengMingdan.selection()[0]
            xueshengJiafen=treeXueshengMingdan.item(item,'values')[0]
            sqlJiafen="INSERT INTO tiwen(xuehao,shijian.defen)VALUES('"+xuehaoJiafen+"','"+common.getCurrrentDateTime()+"',5)"
            Common.doSQL(sqlJiafen)
            tkinter.messagebox.showinfo('恭喜','加分成功')
        buttonJiafen=tkinter.Button(self.top,text='听课认真加分',command=buttonJiafenClick)
        buttonJiafen.place(x=30,y=350,height=20,width=100)
        def buttonJianfenClick():
            if nottreeXueshengMingdan.selection():
                tkinter.messagebox.showerror('很抱歉','请选择学生')
                return
            item=treeXueshengMingdan.selection()[0]
            xueshengJianfen=treeXueshengMingdan.item(item,'values')[0]
            sqlJianfen="INSERT INTO tiwen(xuehao,shijian.defen)VALUES('"+xuehaoJiafen+"','"+common.getCurrrentDateTime()+"',-5)"
            Common.doSQL(sqlJiafen)
            tkinter.messagebox.showinfo('恭喜','减分成功')
        buttonJianfen=tkinter.Button(self.top,text='听课不认真减分',command=buttonJiafenClick)
        buttonJianfen.place(x=30,y=350,height=20,width=100)
        labelTishi.place(x=10,y=380,height=20)
