#!usr/bin/python
#编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个为最小公倍数
def demo(m,n):
    if m>n:
        m,n=n,m
    p=m*n
    while m!=0:
        r=n%m
        n=m
        m=r
    return(n,int(p/n))
print(demo(20,30))
