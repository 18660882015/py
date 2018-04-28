#!usr/bin/python
#conding=utf-8
from xlwt import *

book=Workbook()
sheet1=book.add_sheet("First")
al=Alignment()
al.horz=Alignment.HORZ_CENTER
al.vert=Alignment.VERT_CENTER
borders=Borders()
borders.bottom=Borders.THICK
style=XFStyle()
style.alignment=al
Style.borders=borders
row0=sheet1.row(0)
row0=write(0,'test',style=style)
book.save(r'D:test.xls')
print('使用xlwt模块写入Excel文件,xlwt为excel2003之前的python扩建库，默认无安装')
