#!usr/bin/python
#conding=utf-8
def buttonDaoreTikuClick():
    filename=tkinter.filedialog.askopenfilename(title='请选择 Excel 2003 或Word 2007版本的题库文件',filetypes=[('Excel Files','*.xls'),('word 2007 Files','*.docx')])
    if filename:
        if filename.endswith('.xls'):
            workbook=xlrd.open_workbook(filename=filename)
            sheet1=workbook.sheet_by_index(0)
            if sheet1.ncols !=4:
                tkinter.messagebox.showerror(title='抱歉',message='题库格式不对')
                return
            for rowIndex in range(1,sheet1.nrows):
                row=sheet1.row(rowIndex)
                sql="INSERT INTO tiku(kechengmingcheng,zhangjie,timu,daan)VALUES('"+str(row[0].value).strip()+"','"+str(row[1].value)+"','"+str(row[2].value)+"','"+str(row[3].value)+"')"
                Common.doSQL(sql)
            tkinter.messagebox.showinfo(title='恭喜',message='导入成功')
        elif filename.endswith('.docx'):
            from docx import Document
            doc=Document(filename)
            conn=sqlite3.connect('database.db')
            cur=conn.cursor()
            cur.execute('delete from tiku')
            conn.commit()
            for p in doc.paragraphs:
                text=p.text
                if'('in text and')'in text:
                    index=text.index('(')
                    question=text[:index]
                    if '___'in question:
                        question='填空题:'+question
                    else:
                        question='判断题:'+question
                    answer=text[index+1:-1]
                    sql='INSERT INTO tiku(kechengmingcheng,zhangjie,timu,daan)VALUES("python 程序设计","未分类","'+question+'","'+answer+'")'
                    cur.execute(sql)
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo(title='恭喜',message='导入成功')
buttonDaoruTiku = tkinter.Button (root, text = '导入题库',command = buttonDaoruTikuClick)
buttonDaoruTiku.place(x=20,y=220,height=30,width=100)
                                                         
