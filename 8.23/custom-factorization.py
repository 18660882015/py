#!usr/bin/python
#编写程序，对整数进行因式分解
from random import randint
from math import sqrt
n=int(input('input a integer'))
def factoring(n):
    if not isinstance(n,int):
        print('you must give me an integer')
        return
    #检验n是否为整数
    result=[]
    for p in primes:
        while n!=1:
            if n%p==0:
                n=n/p
                result.append(p)
            else:
                print('you input a prime number')
                break
        else:
            result=map(str,result)
            result='*'.join(result)
            return result
    if not result:
        return n
testData=[randint(10,100000)for i in range(10)]
maxData=max(testData)
primes=[p for p in range(2,maxData)if 0 not in [p%d for d in range(2,int(sqrt(p))+1)]]
r=factoring(n)
print(n,'=',r)
print(n==eval(r))
