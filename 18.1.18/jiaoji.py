#!usr/bin/python
#conding=utf-8
a_list=list(input('input a_list'))
b_list=list(input('input b_list'))
c_list=list(input('input c_list'))
def ab_two():
    result=[]
    for item in a_list:
        if item in b_list:
            result.append(item)
    print (result)
def bc_two():
    result=[]
    for item in b_list:
        if item in c_list:
            result.append(item)
    print (result)
def ac_two():
    result=[]
    for item in a_list:
        if item in c_list:
            result.append(item)
    print (result)
def three():
    result=[]
    for item in a_list:
        if item in b_list:
            if item in c_list:
                result.append(item)
    print (result)
def xuanze():
    print('输入1为ab交集，输入2为bc交集，输入3为ac交集，输入4为abc交集')
    key=int(input('input 1,2,3 or 4'))
    if key==1:
        ab_two()
    if key==2:
        bc_two()
    if key==3:
        ac_two()
    if key==4:
        three()
xuanze()   
