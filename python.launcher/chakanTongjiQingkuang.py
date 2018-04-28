#!usr/bin/python
#conding=utf-8
class windowChakanTongjiQingkuang:
    def __init__(self,root,myTitle):
        self.top=tkinter.Toplevel(root,width=600,height=380)
        self.top.title(myTitle)
        self.top.attributes('-topmost',1)
        xueshnegZhuanye=Common.getZhuanye()
        comboboxZhaunye=tkinter.ttk.Combobox(self.top,values=xueshengZhuanye)
        comboboxZhangye.place(x=20,y=20,height=20,width=120)
    def chakanZhuangye():
        zhuanye=comboboxZhuangye.get()
        if notzhuangye:
            tkinter.messagebox.showerror('很抱歉','请选择专业')
            return
        else:
            xuehaoXingmings=Common.getXuehaoXingming(zhuanye)
            xuehaos=[xingming.split(',')[0]for xingming in xuehaoXingmings]
            xingmings=[xingming.split(',')[1]for xingming in xuehaoXingmings]
            chuqinCishu=[Common.getChuqinCishu(xuehao)for xuehao in xuehaos]
            tiwenDefen=[Common.getTiwenDefen(xuehao)for xuehao in xuehaos]
            zhuadongTiwenCishu=[Common.getZhudongTiwenCishu(xuehao)for xuehao in xuehaos]
            kaoshidefen=[Common.getKaoshiDefen(xuehao)for xuehao in xuehaos]
            for row in treeXueshengMingdan.get_children():
                treeXueshengMingdan.delete(row)
            iii=0
            tj=zip(xuehaos,xingmings,chuqinCishu,tiwenDefen,zhudongTiwenCishu,kaoshidefen)
            for xuehao,xingming,chuqin,tiwen,zhudongtiwen,kaoshidefen in tj:
                treeXueshengMingdan.insert('',iii,values=(xuehao,xingming,chuqin,tiwen,zhuandongtiwen,kaoshidefen))
                iii=iii+1
    buttonZhuanye=tkinter.Button(self.top,text='查看',command=chakanZhuanye)
    buttonZhuanye.place(x=150,y=20,height=20,width=80)
    self.frame=tkinter.Frame(self.top)
    self.frame.place(x=20,y=50,width=560,height=320)
    scrollBar=tkinter.Scrollbar(self.frame)
    scrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    treeXueshengMingdan=tkinter.ttk.Treeview(self.frame,columns=('col1',
    'col2','col3','col4','col5','col6'),
                                             show="headings",
                                             yscrollcommand=scrollBar.set)
    treeXueshengMingdan.colum('col1',width=70,anchor='center')
    treeXueshengMingdan.colum('col2',width=50,anchor='center')
    treeXueshengMingdan.colum('col3',width=120,anchor='center')
    treeXueshengMingdan.colum('col4',width=120,anchor='center')
    treeXueshengMingdan.colum('col5',width=80,anchor='center')
    treeXueshengMingdan.colum('col6',width=80,anchor='center')
    treeXueshengMingdan.heading('col1',text='学号')
    treeXueshengMingdan.heading('col2',text='姓名')
    treeXueshengMingdan.heading('col3',text='出勤次数')
    treeXueshengMingdan.heading('col4',text='老师提问得分')
    treeXueshengMingdan.heading('col5',text='主动提问得分')
    treeXueshengMingdan.heading('col6',text='考试得分')
    treeXueshengMingdan.pack(side=tkinter.LEFT,fill=tkinter.Y)
    scrollBar.config(command=treeXueshengMingdan.yview)
    
        
