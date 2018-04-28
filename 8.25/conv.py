#!usr/bin/python
#coding=utf-8
def conv(lst1,lst2):
    result=[]
    lst1.reverse()
    length1=len(lst1)
    length2=len(lst2)
    for i in range(1,length1+1):
        t=lst1[length1-i:]
        v=sum((item1*item2 for item1,item2 in zip(t,lst2)))
        result.append(v)
    for i in range(1,length2):
        t=lst2[i:]
        v=sum((item1*item2 for item1,item2 in zip(lst1,t)))
        result.append(v)   
    return result
def mul(lst):
    result=''
    c=0
    for item in lst[::-1]:
        item=item+c
        n,c=str(item%10),item//10
        result+=n
    if c:
        result+=str(c)
    return eval(result[::-1])
def main (num1,num2):
    lst1=list(map(int,str(num1)))
    lst2=list(map(int,str(num2)))
    result=conv(lst1,lst2)
    print(mul(result)==num1*num2)
from random import randint
for i in range(100):
    num1=randint(1,99999999)
    num2=randint(1,99999999999)
    main(num1,num2)
