#!usr/bin/python
#conding=utf-8
int_canDianming=tkinter.IntVar(root,value=0)
def thread_Dianming():
    global sockDianming
    sockDianming=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockDianming.bind(('',30000))
    sockDianming.listen(200)
    while int_canDianming.get()==1:
        try:
            conn,addr=sockDianming.accept()
        except:
            return
        data=conn.recv(1024)
        data=data.decode()
        xuehao,xingming=data.split(',')
        sqlIfMatch="SELECT count(xuehao)FROM students WHERE xuehao='"+xuehao+"'AND xingming='"+xingming+"'"
        if Common.getDataBySQL(sqlIfMatch)[0][0]!=0:
            conn.sendall('notmatch',encode())
            conn.close()
        else:
            sqlShifouDaiDianming="SELECT count(ip)FROM dianming WHERE ip='"+addr[0]+"'AND shijian >='"+startTime+"'"
            if Common.getDataBySQL(sqlShifouDaiDianming)[0][0] !=0:
                conn.sendall('daidianming'.encode())
                conn.close()
            else:
                sqlDianming="INSERT INTO dianming (xuehao,shijian,ip)VALUES('"+xuehao+"','"+currentTime+"','"+addr[0]+"')"
                Common.doSQL(sqlDianming)
                conn.sendall('ok'.encode())
                conn.close()
sockDianming.close()
sockDianming=None
