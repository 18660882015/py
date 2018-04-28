#itertools中permutations()cycle()compress()groupby()函数的使用
import itertools
x='Private Key'
y=itertools.cycle(x)
for i in range(20):
    print(next (y),end=',')
for i in range(5):
    print(next (y),end=',')
x=range(1,20)
y=(1,0)*9+(1,)
list(itertools.compress(x,y))
def group(v):
    if v>10:
        return 'greater than 10'
    elif v<5:
        return 'less than 5'
    else:
        return 'between 5 and 10'
x=range(20)
y=itertools.groupby(x,group)
for k,v in y:
    print (k,':',list(v))
list(itertools.permutations([1,2,3,4],3))
x=(itertools.permutations([1,2,3,4],3))
next(x)
next(x)
next(x)


