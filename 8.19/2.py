#!usr/bin/python
#in在列表，集合，字典中的运算速度
import random
import time
x=list(range(10000))
y=set(range(10000))
z=dict(zip(range(1000),range(10000)))
r=random.randint(0,9999)


start=time.time()
for i in range(9999999):
    r in x
print('list,time used:',time.time()-start)


start=time.time()
for i in range(9999999):
    r in y
print('set,time used:',time.time()-start)


start=time.time()
for i in range(9999999):
    r in z
print('dict,time used:',time.time()-start)
