#!usr/bin/python
#conding=utf-8
def thread_xueshengKaoshiMain():
    global sockKaoshi
    sockKaoshi=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockKaoshi.bind(('',18000))
    sockKaoshi.listen(200)
    while int_xueshengKaoshi.get()==1:
        try:
            conn,addr=sockKaoshi.accept()
        except:
            return
        t_Kaoshi=threading.Thread(target=thread_xueshengKaoshi,args=(conn,))
        t_Kaoshi.start()
    sockKaoshi.close()
def thread_xueshengKaoshi(conn):
    data=conn.recv(1024)
    data=data.decode()
    xuehao,xingming=data.split(',')
    sql=("SELECT count(xuehao)FROM studnts WHERE xuehao='"+xuehao.strip()+"'AND xingming='"+xingming.strip()+"'")
    t=Common.getDataBySQL(sql)[0][0]
    if t!=1:
        conn.sendall('notmatch'.encode())
        conn.close()
        return
    else:
        conn.sendall('ok'.encode())
    sqlKechengmingcheng="SELECT distinct(kechengmingcheng)FROM tiku"
    kechengQingdan=[]
    for kecheng in Common.getDataBySQl(sqlKechengmingcheng):
        kechengQingdan.append(str(kecheng[0]))
    kechengQingdan=','.join(kechengQingdan)
    conn.sendall(kechengQingdan.encode())
    while int_xueshengKaoshi.get()==1:
        data=conn.recv(1024)
        data.data.decode()
        if data =='xxxx':
            conn.recv(1024)
            break
        kechengmingcheng,currentID,daan,pre_next=data.split('xx')
        if pre_next=='next':
            if currentID !='0':
                if daan ==biaozhundaan:
                    shifouzhengque='Y'
                elif ''.join(biaozhundaan.split())==''.join(daan.split()):
                    shifouzhengque='Y'
                elif biaozhundaan.endswith('()')and daan==biaozhundaan[:-2]:
                    shifouzhengque='Y'
                elif''.join(biaozhundaan.split())==''.join(daan.split()):
                    shifouzhengque='Y'
                else:
                    shifouzhengque='N'
                sql=('INSERT INTO kaoshi(xuehao,xingming,timubiaohao,xueshengdaan,biaozhundaan,shifouzhengque,shijian)VALUES("'+xuehao+'","'+xingming+'",'+currentID+',"'+daan+'","'+biaozhundaan+'","'+shifouzhengque+'","'+common.getCurrentDataTime()+'")')
                Common.doSQL(sql)
            sql="SELECT count(xuehao)FROM kaoshi WHERE xuehao='"+xuehao+"'"
            total=Common.getDataBySQL(sql)[0]
            if total[0]>=100:
                conn.sendall(('no,'+str(Common.getKaoshiDefen(xuehao))).encode())
                break
            sqlHasMore=('SELECT kechengmingcheng,zhangjie,timu,id,daan FROM tiku WHERE kechengmingcheng='"+kechengmingcheng+"'AND id NOT IN (SELECT timubianhao FROM kaoshi WHERE xuehao='"+xuehao"')ORDER BY random()limit 1')
            ttt=Common.getDataBySQL(sqlHasMore)
            if ttt:
                tttt=ttt[0]
                message=tttt[0]+'xx'+tttt[1]+'xx'+tttt[2]+'xx'+str(tttt[3])
                biaozhundaan=str(tttt[4])
                conn.sendall(message.encode())
            else:
                conn.sendall(('no,'+str(Common.getKaoshiDefen(xuehao))).encode())
    conn.close()               
