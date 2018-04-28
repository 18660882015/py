#!usr/bin/python
#coding=utf-8
from random import randint
def guess():
    value=randint(1,100)
    maxTime=5
    print ('Must input an integer between 1 and 99')
    for i in range(maxTime):
        prompt='Start to GUESS:'if i==0 else'Guess again:'
        try:
            x=int(input(prompt))
            if x==value:
                print('Congratulations!')
                break
            elif x>value:
                print('Too big')
            else:
                print('Too little')
        except:
            print ('Must input an integer between 1 and 99')
    else:
        print('Game Over.Fall')
        print('The value is:',value)
guess()
