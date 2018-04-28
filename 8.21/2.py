#!usr/bin/python
#编写函数，接收一个正偶数为参数，输出两个素数，且两素树之和等于原来的正偶数，若存在多组，则全部输出
import math
def IsPrime(n):
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0:
            return False
        return True
def demo(n):
    if isinstance(n,int)and n>0 and n%2==0:
        for i in range(3,int(n/2)+1):
            if i%2==1 and IsPrime(i)and IsPrime(n-i):
                print(i,'+',n-i,'=',n)
demo(60)
