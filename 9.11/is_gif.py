#!usr/bin/python
#conding=utf-8
print('不依赖文件拓展名来判断是否为gif格式')
def is_gif(fname):
    f=open(fname,'r')
    first4=type(f.read(4))
    f.close()
    return first4==('G','I','F','8')
s=str(input('input filename'))
is_gif(s)
