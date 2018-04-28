#!usr/bin/python
#conding=utf-8
class simNumpyArray(object):
    def __init__(self,p):
        if type (p) not in(list,tuple,range):
            print ('data type error')
            return
        for item in p:
            if type (item) not in(int,float,complex):
                print('data type error')
                return
        self.__data=[list(p)]
        self.__row=1
        self.__col=len(p)
    def __del__(self):
        del self.__data
    def reshape(self,size):
        if not (isinstance(size,list)or isinstance(size,tuple)):
            print ('size parameter error')
            return
        if len(size)!=2:
            print ('size paramter error')
            return
        if (not isinstance(size[0],int))or(not isinstance(size[1],int)):
            print ('size paramter error')
            return
        if size[0] !=-1 and size [1] !=-1 and size[0] * size[1] !=self.__row * self.__col:
            print ('size paramter error')
            return
        if size[0] == -1:
            if size[1] ==-1 or(self.__row * self.__col)%size[1] !=0:
                print ('size paramter error')
                return
        if size[1] == -1:
            if size[0] ==-1 or(self.__row * self.__col)%size[0] !=0:
                print ('size paramter error')
                return
        data=[t for i in self.__data for t in i]
        if size[0] ==-1:
            self.__row=int(self.__row * self.__col/size[1])
            self.__col=size[1]
        elif size[1] ==-1:
            self.__col=int(self.__row * self.__col/size[0])
            self.__row=size[0]
        else:
            self.__row=size[0]
            self.__col=size[1]
        self.__data=[[data[row*self.__col+col] for col in range(self.__col)]
        for row in range(self.__row)]
    def __repr__(self):
        for i in self.__data:
            print(i)
            return ''
    def __str__(self):
        return '\n'.join(map(str,self.__data))
    @property
    def T(self):
        b=simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row,self.__col))
        b.__data=list(map(list,zip(*b.__data)))
        b.__row,b.__col=b.__col,b.__row
        return b
    def __operate(self,n,op):
        b=simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row,self.__col))
        b.__data=[[eval(str(j)+op+str(n))for j in item]for item in b.__data]
        return b
    def __matrixAddSub(self,n,op):
        c=simNumpyArray([1])
        c.__row=self.__row
        c.__col=self.__col
        c.data=[[eval(str(x[i])+op+str(y[i]))for i in range(len(x))]for x,y
                in zip(self.__data,n.__data)]
        return c
    def __add__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'+')
        elif isinstance(n,simNumpyArray):
            if n.__row==self.__row and n.__col==self.__col:
                return self.__matrixAddSub(n,'+')
            else:
                print('two matrix must be the same size')
                return
        else:
            print('data type error')
            return
    def __sub__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'-')
        elif isinstance(n,simNumpyArray):
            if n.__row==self.__row and n.__col==self.__col:
                return self.__matrixAddSub(n,'-')
            else:
                print ('two matrix must be the same size')
                return
        else:
            print('data type error')
            return
    def __mul__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'*')
        elif isinstance(n,simNumpyArray):
            if n.__row==self.__col:
                data=[]
                for row in self.__data:
                    t=[]
                    for ii in range(n.__col):
                        col=[c[ii] for c in n.__data]
                        tt=sum([i*j for i,j in zip(row,col)])
                        t.append(tt)
                    data.append(t)
                c=simNumpyArray([t for i in data for t in i])
                c.reshape((self.__row,n.__col))
                return c
            else:
                print ('size error')
                return
        else:
            print('data type error')
            return
    def __truediv__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'/')
        else:
            print ('data error')
            return
    def __floordiv__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'//')
        else:
            print ('data error')
            return
    def __pow__(self,n):
        if type(n)in(int,float,complex):
            return self.__operate(n,'**')
        else:
            print ('data error')
            return
    def __eq__(self,n):
        if isinstance(n,simNumpyArray):
            if self.__data==n.__data:
                return True
            else:
                return False
        else:
            print('data error')
            return
    def __lt__(self,n):
        if isinstance(n,simNumpyArray):
            if self.__data<n.__data:
                return True
            else:
                return False
        else:
            print('data error')
            return
    def __contains__(self,v):
        if v in self.__data:
            return True
        else:
            return False
    def __iter__(self):
        return iter(self.__data)
    def __triangle(self,method):
        try:
            b=simNumpyArray([t for i in self.__data for t in i])
            b.reshape((self.__row,self.__col))
            b.__data=[[eval("__import__('math')."+method+"("+str(j)+")")for j in
                       item]for item in b.__data]
            return b
        except:
            return 'method error'
    @property
    def Sin(self):
        return self.__triangle('sin')
    @property
    def Cos(self):
        return self.__triangle('cos')
        
            
  
