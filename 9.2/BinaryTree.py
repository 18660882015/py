#!usr/bin/python
#conding=utf-8
class BinaryTree:
    def __init__(self,value):
        self.__left=None
        self.__right=  None
        self.__data=value
    def __del__(self):
        del self.__data
    def insertLeftChild(self,value):
        if self.__left:
            print ('Left child tree already exists.')
        else:
            self.__left=BinaryTree(value)
            return self.__left
    def insertRightChild(self,value):
        if self.__right:
            print ('Right child tree already exists.')
        else:
            self.__right=BinaryTree(value)
            return self.__right
    def show(self):
        print (self.__data)
    def preOrder(self):
        print(self.__data)
        if self.__left:
            self.__left.perOrder()
        if self.__right:
            self.__right.perOrder()
    def postOrder(self):
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print(self.__data)
    def inOrder(self):
        if self.__left:
            self.__left.inOrder()
        print(self.__data)    
        if self.__right:
            self.__right.inOrder()
if __name__=='__main__':
    print('please use me as a module.')
    
    
