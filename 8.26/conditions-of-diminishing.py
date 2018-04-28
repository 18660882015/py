#!usr/bin/python
#conding=utf-8
from itertools import cycle
def demo(lst,k):
    t_lst=lst[:]
    while len(t_lst)>1:
        c=cycle(t_lst)
        for i in range(k):
            t=next(c)
        index=t_lst.index(t)
        t_lst=t_lst[index+1:]+t_lst[:index]
        print(t_lst)
    return t_lst[0]
lst=list(range(1,11))
print(demo(lst,3))
