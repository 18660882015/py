#!usr/bin/python
#coding=utf-8
#1.电话本查询，随机生成100个电话号码及对应姓名，能根据姓名查询电话
#2.让这个程序有更新功能，能增加新的电话-姓名对
#3.假设你有这些姓名对应的邮箱，将邮箱信息合并到电话信息中，即提供姓名，
#      输出姓名-电话-邮箱
import random
import string
keys=[]
values=[]
key=[]
value=[]
for i in range(1,101):
    a_str=[random.choice(string.ascii_uppercase)for i in range(4)]
    key=''.join(a_str)
    keys.append(key)
    b_str=[random.choice(string.digits)for j in range(11)]
    value=''.join(b_str)
    values.append(value)
a_dict=dict(zip(keys,values))
if len(a_dict)!=100:
    j=100-len(a_dict)
    for k in range(j):
        a_str=[random.choice(string.ascii_uppercase)for i in range(4)]
        key=''.join(a_str)
        keys.append(key)
        b_str=[random.choice(string.digits)for j in range(11)]
        value=''.join(b_str)
        values.append(value)
        a_dict(keys,values)
else:
    pass
b_dict=dict(zip(a_dict.values(),a_dict.keys()))
if len(b_dict)!=100:
    j=100-len(b_dict)
    for k in range(j):
        a_str=[random.choice(string.ascii_uppercase)for i in range(4)]
        key=''.join(a_str)
        keys.append(key)
        b_str=[random.choice(string.digits)for j in range(11)]
        value=''.join(b_str)
        values.append(value)
        b_dict(values,keys)
        a_dict=dict(zip(b_dict.kays,b_dict.values))
        
else:
    pass
print (a_dict)
def go_back():
    print ('end or continue')
    print ('end: input 1')
    print ('continue: input 2')
    i=int(input('input 1 or 2'))
    if i==1:
        pass
    else:
        xuanze()
def add():
    keys=str(input('input a name'))
    values=str(input('input a number'))
    a_dict.setdefault(keys,values)
    print (a_dict)
    go_back()
def address():
    keys=str(input('input a name'))
    p=str(input('input a address'))
    value=a_dict[keys]
    if keys in a_dict:
        a_dict.update({keys:(value+p)})
        print (a_dict)
        go_back()
    else:
        print ('The keys not in a_dict ')
        go_back()
def piliang():
    keys=str(input('input name'))
    n=int(input('input you need how many'))
    list=keys.split()
    for i in range(0,n):
        v=a_dict[list[i]]
        print (list[i])
        print (v)
    go_back()           
def xuanze():
    print ('Please select the following options 1,2 or 3')
    print ('1.Query function')
    print ('2.Add new contacts')
    print ('3.Add the address to the contact')
    n=int(input())
    if n==1:
        piliang()
    elif n==2:
        add()
    else:
        address()
xuanze()
   


