#!usr/bin/python
#conding=utf-8
def hannuo(num,src,dst,temp=None):
    global times
    assert type(num)==int,'num must be integer'
    assert num>0,'num must>0'
    if num==1:
        print ('The {0} Times move:{1}==>{2}'.format(times,src,dst))
        times+=1
    else:
        hannuo(num-1,src,temp,dst)
        hannuo(1,src,dst)
        hannuo(num-1,temp,dst,src)
times=1
num=int(input('input a num'))
src=str(input('input src is: '))
dst=str(input('input dst is: '))
temp=str(input('input temp is:'))
hannuo(num,src,dst,temp)
            
