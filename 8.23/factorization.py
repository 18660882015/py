#!usr/bin/python
#编写程序，对整数进行因式分解
from random import randint
from math import sqrt
def factoring(n):
    '''对大数进行因式分解'''
    if not isinstance(n,int):
        print('you must give me an integer')
        return
    result=[]
    for p in primes:
        while n!=1:
            if n%p==0:
                n=n/p
                result.append(p)
            else:
                break
        else:
            result=map(str,result)
            result='*'.join(result)
            return result
    if not result:
        return n
testData=[randint(10,100000)for i in range(50)]
maxData=max(testData)
primes=[p for p in range(2,maxData)if 0 not in [p%d for d in range(2,int(sqrt(p))+1)]]
for data in testData:
    r=factoring(data)
    print(data,'=',r)
    print(data==eval(r))
