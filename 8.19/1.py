#!usr/bin/python
#内置函数sorted（）的使用
phonebook={'linda':'7750','bob':'9340','carol':'5834'}
from operator import itemgetter
sorted(phonebook.items(),key=itemgetter(1))
[('carol','5834'),('linda','7750'),('bob','9345')]
sorted(phonebook.items(),key=itemgetter(0))
[('bob','9345'),('carol','5834'),('linda','7750')]
sorted(phonebook.items(),key=lambda item:item[0])
[('bob','9345'),('carol','5834'),('linda','7750')]
persons=[{'name':'dong','age':37},
         {'name':'zhang','age':40},
         {'name':'li','age':50},
         {'name':'dong','age':43}]
print(persons)
           #结果[{'age':37,'name':'dong'},{'age':40,'name':'zhang'},{'age':50,'name':'li'},{'age':43,'name':'dong'}]
print(sorted(persons,key=lambda x:(x['name'],-x['age'])))
           #按名称升序，按年龄降序
           #结果[{'age':37,'name':'dong'},{'age':40,'name':'zhang'},{'age':50,'name':'li'},{'age':43,'name':'dong'}]
