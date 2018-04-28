#!usr/bin/python
#conding=utf-8
class Set(object):
    def __init__(self,data=None):
        if data==None:
            self.__data=[]
        else:
            if not hasattr(data,'__iter__'):
                raise Exception('必须提供可迭代数据类型')
            temp=[]
            for item in data:
                hash(item)
                if not item in temp:
                    temp.append(item)
                    self.__data=temp
    def add(self,value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('元素已存在，操作被忽略')
    def remove(self,value):
        if value in self.__data:
            self.__data.remove(value)
            print('删除成功')
        else:
            print('元素不存在，删除操作被忽略')
    def pop(self):
        if not self.__data:
            print('集合已空，弹出操作被忽略')
            return
        import random
        item=random.choice(self.__data)
        print(item)
        self.__data.remove(item)
    def __sub__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        result=Set()
        for item in self.__data:
            if item not in anotherSet.__data:
                result.__data.append(item)
        return result
    def difference(self,antherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        return self-anotherSet
    def __or__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        result=Set(self.__data)
        for item in anotherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result
    def union(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        return self |anotherSet
    def __and__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        result=[]
        for item in self.__data:
            if item in anotherSet.__data:
                result.__data.append(item)
        return result
    def __xor__(self,anotherSet):
        return(self-anotherSet)|(anotherSet-self)
    def symetric_difference(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        return self^anotherSet
    def __eq__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        if sorted(self.__data)==sorted(anotherSet.__data):
            return True
        else:
            return False
    def __gt__(self,anotherSet):
        if not isinstance(anoterSet,Set):
            raise Exception('类型错误')
        if self !=anotherSet:
            flag1=True
            for item in self.__data:
                if item not in anotherSet.__data:
                    flag1=False
                    break
                flag2=True
                for item in anotherSet.__data:
                    if item not in self.__data:
                        flag2=False
                        break
                if not flag1 and flag2:
                    return True
                return False
    def __ge__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        return self==anotherSet or self>anotherSet
    def issubset(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        if self<anotherSet:
            return True
        else:
            return False
    def issuperset(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception('类型错误')
        if self>anotherSet:
            return True
        else:
            return False
    def clear(self):
        while self.__data:
            del self.__data[-1]
        print ('集合已清空')
    def __iter__(self):
        return iter(self.__data)
    def __contains__(self,value):
        if value in self.__data:
            return True
        else:
            return False
    def __len__(self):
        return len(self.__data)
    def __repr__(self):
        return '{'+str(self.__data)[1:-1]+'}'
    def __str__(self):
        return '{'+str(self.__data)[1:-1]+'}'
