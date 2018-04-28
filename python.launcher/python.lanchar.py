#!usr/bin/python
#coding=utf-8
import datetime
import tkinter
import tkinter.scrolledtext
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
import socket
import sqlite3
import random
import threading
import time
import struct
import os
import sys
import string
path='"'+os.path.dirname(sys.executable)+\
      '\\scripts\\pip"install --upgrade pip'
os.system(path)
try:
    import docx
except:
    path='"'+os.path.dirname(sys.executable)+\
          '\\scripts\\pip"install python-docx'
    os.system(path)
    import docx
try:
    import xlrd
except:
    path='"'+os.path.dirname(sys.executable)+'\\scripts\\pip"install xlrd'
    os.system(path)
    import xlrd
try:
    import openpyxl
except:
    path='"'+os.path.dirname(sys.executable)+\
          '\\scripts\\pip"install openpyxl'
    os.system(path)
    import openpyxl
root=tkinter.Tk()
#root.config(width=360)
#root.config(height=260)
root.geometry('360*340+400+300')
root.resizable(False,False)
root.title('边讲边练类课程教学管理系统  v1.0---董付国')
def closeWindows():
    if int_canDianming.get()==1:
        int_canDianming.set(0)
    if int_zuoye.get()==1:
        int_zuoye.set(0)
    if int_xueshengTiwen.get()==1:
        int_xueshengTiwen.set(0)
    if int_server.get()==1:
        int_server.set(0)
    root.destory()
root.protocol('WM_DELETE_WINDOW',closewindow)
class Common:
    def getZhuanye():
        conn=sqlites3.connect('database.db')
        cur=conn.cursor()
        cur.execte('SELECT distinct(zhuanye)FROM students')
        temp=cur.fetchall()
        conn.close()
        xueshengZhuanye=[]
        for line in temp:
            xueshengZhuanye.append(line[0])
        return xueshengZhuanye
    def getXuehaoXingming(zhuanye):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute("SELECT xuehao,xingming FROM students WHERE zhuanye='"+zhuanye+"'ORDER BY xuehao")
        temp=cur.fetchall()
        conn.close()
        xueshengXinxi=[]
        for line in temp:
            xueshengXinxi.append(line[0]+','+line[1])
        return xueshengXinxi
    def getChuqinCishu(xuehao):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute("SELECT count(xuehao)FROM dianming WHERE xuehao='"+xuehao+"'")
        temp=cur.fetchall()
        conn.close()
        xueshengXinxi=[]
        for line in temp:
            xueshengXinxi.append(line[0])
        return xueshengXinxi
    def getTiwenDefen(xuehao):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute("SELECT sum(defen)FROM tiwen WHERE xue hao='"+xuehao+"'")
        temp=cur.fetchall()
        conn.close()
        xueshengXinxi=[]
        for line in temp:
            xueshengXinxi.append(line[0])
        return xueshengXinxi
    def getZhudongTiwenCishu(xuehao):
        conn=sqlite3.connect(database.db)
        cur=conn.cursor()
        cur.execute('SELECT count(xuehao)FROM xueshengtiwen WHERW xuehao='"+xuehao+"'AND wenti NOT LIKE "老师回复%"')
        temp=cur.fetchall()
        conn.close()
        xueshnegXinxi=[]
        for line in temp:
            xueshengXinxi.append(line[0])
        return xueshengXinxi
    def getKaoshiDefen(xuehao):
        conn=sqlite3.connect('database.db')
        cur.execute("SELECT count(xuehao)FROM kaoshi WHERE xuehao='"+xuehao+"'AND shifouzhengque='Y'")
        temp=cur.fetchall()
        conn.close()
        xueshengkaoshi=[]
        for line in temp:
            xueshengkaoshi.append(line[0])
        return xueshengkaoshi
    def getDataBySQL(sql):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        conn.close
        return result
    def doSQL(sql):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute(sql)
        result=cur.fetchall()
        conn.close
        return result
    def doSQL(sql):
        conn=sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    def getCurrentDatetime():
        return str(datetime.datetime.now())[:19]
    def getStartDateTime():
        now=datetime.datatime.nows()
        now=now+datetime.timedelta(minutes=-90)
        return str(now)[:19]
        
        
