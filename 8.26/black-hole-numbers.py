#!usr/bin/python
#conding=utf-8
def main(n):
    start=10**(n-1)+2
    end=start*10-20
    for i in range(start,end):
        i=str(i)
        big=''.join(sorted(i,reverse=True))
        big=int(big)
        little=''.join(sorted(i))
        little=int(little)
        if big-little==int(i):
            print(i)
n=int(input('input a num n'))
main(n)
