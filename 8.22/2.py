#!usr/bin/python
#8.22.1的简洁代码
import random
def demo(x,n):
    t1=[i for i in x if i<n]
    t2=[i for i in x if i>n]
    return t1+[n]+t2
x=list(range(1,10))
random.shuffle(x)
x
demo(x,4)
