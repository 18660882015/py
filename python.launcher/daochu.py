#!usr/bin/python
#conding=utf-8
def buttonDaochuClick():
    try:
        import openpyxl
        from openpyxl import Workbook
    except:
        tkinter.messagebox.showerror('抱歉','您需要安装openpyxl拓展库')
    wb=Workbook()
    wb.remove_sheet(wb.worksheets[0])
    ws=wb.create_sheet(title='在线点名情况')
    ws.append(['学号','姓名','点名时间'])
    sql='SELECT students.xuehao,students.xingming,shijian FROM students,dianming WHERE students.xuehao=dianming.xuehao ORDER BY students.xuehao'
    data=Common.getDataBySQl(sql)
    for d in data:
        ws.append([d[0],d[1],d[2]])
    wb.save('数据导出.xlsx')
    tkinter.messagebox.showinfo('恭喜','导出成功，请查看“数据导出.xlsx”文件')
buttonDaochu=tkinter.Button(root,text='数据导出',command=buttonDaochuClick)
buttonDaochu.place(x=240,y=260,height=30,width=100)
