#!usr/bin/python
#coding=utf-8
def demo(v,n):
    assert 0<v<10,'v must between 1 and 9'
    assert type(n)==int, 'n must be integer'
    result,t=0,0
    for i in range(n):
        t=t*10+v
        result+=t
    return result
print('resolve as a+aa+aaa+aaaa.....\'s problem')
v=int(input('input a integer v'))
n=int(input('input a integer n'))
print(demo(v,n))
