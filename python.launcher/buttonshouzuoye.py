#!usr/bin/python
#conding=utf-8
int_zuoye=tkinter.IntVar(root,value=0)
def three_ZuoyeMain():
    today=Common.getCurrentDateTime().split()[0]
    if not os.path.exists(today):
        os.mkdir(today)
    global sockShouzuoye
    sockShouzuoye=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockshouzuoye.bind(('',30300))
    sockShouzuoye.listen(200)
    while int_zuoye.get()==1:
        time.sleep(0.05)
        try:
            conn,addr=sockShouzuoye.accept()
        except:
            return
        t=threading.Thread(target=thread_ShouZuoye,args=(conn,today))
        t.start()
    sock.close()
def thread_ShouZuoye(conn,today):
    BUFSIZE=1024
    FILEINFO_SIZE=struct.calcsize('I128sI')
    fhead=conn.recv(FILEINFO_SIZE)
    filenamelength,filename,filesize=struct.unpack('I128sI',fhead)
    filename=filename.decode()
    filename=filename[:filenamelength]
    ttt=filename.split(',')[0]
    xuehao,xingming=ttt.split('_')
    sql="SELECT count(xuehao)FROM students WHERE xuehao='"+xuehao.strip()+"'AND xingming='"+xingming.strip()+"'"
    t=Common.getDataBySQL(sql)[0][0]
    if t!=1:
        conn.sendall('notmatch'.encode())
        conn.close()
        return
    else:
        conn.sendall('ok'.encode())
    filename=filename[:-4]+'_'.join(Common.getCurrentDateTime().split())+\
              filename[-4:]
    filename=filename.replace('-','_')
    filename=filename.replace(':','_')
    filename=today+'\\'+filename
    for f in os.listdir(today):
        if f.startswith(ttt):
            os.remove(today+'\\'+f)
    fp=open(filename,'wb')
    restsize=filesize
    while True:
        if restsize>BUFSIZE:
            filedata=conn.recv(BUFSIZE)
        else:
            filedata=conn.recv(restsize)
        if not filedata:
            break
        fp.write(filedata)
        restsize=restsize-len(filedata)
        if restsize==0:
            break
        fp.close()
        conn.close()
    
