#!usr/bin/python
#模拟发红包算法
import random
while True:
    try:
        print('无论num输入的是什么都会变成2')
        total=int(input('input hongbao\'s total'))
        num=int(input('input hongbao\'s num'))
    except:
        continue
    def hongbao(total,num):
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
        for i in range(30):
            each=hongbao(total,num)
            print (each)  
    if type(num)==int:
        break

        
