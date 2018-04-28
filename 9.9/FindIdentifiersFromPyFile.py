#!usr/bin/python
#conding=utf-8
import re
import os
import sys
classes={}
functions=[]
variables={'normal ':{},'paramter':{},'infor':{}}
def _identifyClassNames(index,line):
    pattern=re.compile(r'(?<=class\s)\w+(?=.*?:)')
    matchResult=pattern.search(line)
    if not matchResult:
        return
    className=matchResult.group(0)
    classes[className]=classes.get(className,[])
    classes[className].append(index)
def _identifyFunctionNames(index,line):
    pattern=re.compile(r'(?<=def\s)(\w+)\((.*?)\)(?=:)')
    matchResult=pattern.search(line)
    if not matchResult:
        return
    functionName=matchResult.group(1)
    functions.append((functionName,index))
    parameters=matchResult.group(2).split(r',')
    if parameters[0]=='':
        return
    for v in parameters:
        variables['parameter'][v]=variables['parameter'].get(v,[])
        variables['parameter'][v].append(index)
def _identifyVariableiNames(index,line):
    pattern=re.compile(r'\b(.*?)(?=\s=)')
    matchResult=pattern.search(line)
    if matchResult:
        vs=matchResult.group(1).split(r',')
        for v in vs:
            if 'if' in v:
                v=v.split()[1]
                if '[' in v:
                    v=v[0:v.index('[')]
            variables['normal'][v]=variables['normal'].get(v,[])
            variables['normal'][v].append(index)
    pattern=re.compile(r'(?<=for\s)(.*?)(?=\sin)')
    matchResult=pattern.search(line)
    if mathResult:
        vs=matchResult.group(1).split(r',')
        for v in vs:
            variables['infor'][v]=variables['infor'].get(v,[])
            variables['infor'][v].append(index)
def output():
    print('='*30)
    print('The class name and their line number are:')
    for key,value in classes.item():
        print(key,':',value)
    print('='*30)
    print('The function names and their line numbers are:')
    for i in functions:
        print(i[0],':',i[1])
    print('='*30)
    print('The normal variable names and their line numbers are:')
    for key,value in variables['normal'].item():
        print(key,':',value)
    print('-'*20)
    print('The parameter names and their line numbers in functions are:')
    for key,value in variables['parameter'].item():
        print(key,':',value)
    print('-'*20)
    print('The variable names and their line numbers in for statements are:')
    for key,value in variables['infor'].item():
        print(key,':',value)
def comments(index):
    for i in range(50):
        line=allLines[index+i].strip()
        if line.endswith('""')or line.endswith("''"):
            return i+1
if __name__=='__main__':
    fileName=sys.argv[1]
    #此处应把命令行参数换为文件名
if not os.path.isfile(fileName):
    print('Your input is not a file.')
    sys.exit(0)
if not fileName.endswith('.py'):
    print('Sorry.I can only check Python source file.')
    sys.exit(0)
allLine=[]
with open(fileName,'r')as fp:
    allLines=fp.readlines()
index=0
totalLen=len(allLines)
while index<totalLen:
    line=allLines[index]
    line=line.strip()
    if line.startswith('#'):
        index+=1
        continue
    if line.startswith('""')or line.startswith("''"):
        index+=comments(index)
        continue
    _identifyClassNames(index+1,line)
    _identifyFunctionNames(insex+1,line)
    _identifyVariableNames(index+1,line)
    index+=1
output()
print ('使用方法：python 此文件地址 目标文件地址')
