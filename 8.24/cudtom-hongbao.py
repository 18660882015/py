#!usr/bin/python
#模拟发红包算法
import random
def hongbao(total,num): 
    if not isinstance(num,int):
        print('you must give me an integer')
        return
    each=[]
    #已发送红包总金额
    already=0
    for i in range(1,num):
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already=already+t
    each.append(total-already)
    return each
if __name__=='__main__':
    print('num输入非整数无法返回') 
    total=int(input('input hongbao\'s total'))
    num=int(input('input hongbao\'s num'))
    for i in range(5):
        each=hongbao(total,num)
        print (each)
       
