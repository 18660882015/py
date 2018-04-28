#!usr/bin/python
#conding=utf-8
def buttonImportXueshengXinxiClick():
    filename=tkinter.filedialog.askopenfilename(title='请选择 Excal文件',
                                                filetypes=[('Excal Files','* .xls')])
    if filename:
        workbook=xlrd.open_workbook(filename=filename)
        sheet1=workbook.sheet_by_index(0)
        if sheet1.ncols !=4:
            tkinter.messagebox.showerror(title='抱歉',
                                         message='Excal文件格式不正确')
            return
        for rowIndex in range(1,sheet1.nrows):
            row=sheet1.row(rowIndex)
            sql="INSERT INTO students(xuehao,xingming,zhuanye,kecheng)VALUES('"+str(row[0].value).strip()+"','"+str(row[1].value)+"',,'"+str(row[2].value)+"','"+str(row[3].value)+"')"
            Common.doSQL(sql)
        tkinter.messagebox.showinfo(title='恭喜',message='导入成功')
buttonImportXueshengXinxi=tkinter.Button(root,text='导入学生信息',
                                         common=buttonImportXueshengXinxiClick)
buttonImportXueshengXinxi.place(x=20,y=20,height=30,width=100)
































        
