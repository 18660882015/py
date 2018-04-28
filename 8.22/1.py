#!usr/bin/python
#编写函数，接收一个所有元素值都不相等的整数列表x和一个整数n，要求将值为n的元素作为支点，将列表中所有小于n的值放在n的前方，大于n的放在n的后方
import random
def demo(x,n):
    if n not in x:
        print(n,'is not an element of',x)
        return
    i=x.index(n)
    x[0],x[i]=x[i],x[0]
    key=x[0]
    i=0
    j=len(x)-1
    while i<j:
        while i<j and x[j]>key:
            j-=1
        x[i]=x[j]
        while i<j and x[j]<=key:
            i+=1
        x[j]=x[i]
    x[i]=key
x=list(range(1,10))
random.shuffle(x)
print(x)
demo(x,4)
print(x)
