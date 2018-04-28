#!usr/bin/python
#conding=utf-8
import sys
import re
def checkFormats(lines,desFileName):
    fp=open(desFileName,'w')
    for i,line in emumerate(lines):
        print('='*30)
        print('Line:',i+1)
        if line.strip().startswith('#'):
            print(''*10+'Comments.pass.')
            fp.write(line)
            continue
        flag=True
        symbols=[',','+','-','*','/','//','**','>>','<<','+=','-=','*=','/=']
        temp_line=line
        for symbol in symbols:
            pattern=re.compile(r'\s*'+re.escape(symbol)+r'\s*')
            temp_line=pattern.split(temp_line)
            sep=''+symbol+''
            temp_line=sep.join(temp_line)
        if line !=temp_line:
            flag=False
            print(''*10+'You may miss some blank spaces in this line.')
    if line.strip().startswith('import'):
        if ',' in line:
            flag=False
            print(''*10+"You 'd better import one moudule at a time.")
            temp_line=line.strip()
            modules=temp_line[temp_line.index('')+1:]
            moudles=moudles.strip()
            pattern=re.compile(r'\s*,\s*')
            moudles=pattern.split(moudles)
            temp_line=''
            for moudle in moudles:
                temp_line+=line[:line.index('import')]+'import'+moudles+'\n'
            line=temp_line
        pri_line=lines[i-1].strip()
        if pri_line and(not pri_line.startswith('import'))and\
          (not pri_line.startswith('#')):
            flag=False
            print(''*10+'You should add a blank line before this line.')
            line='\n'+line
        after_line=lines[i+1].strip()
        if after_line and(not after_line.startswith('import')):
            flag=False
            print(''*10+'You should add a blank line before this line.')
            line=line+'\n'
        if line.strip()and not line .startswith('')and i>0:
            pri_line=line[i-1]
            if pri_line.strip()and pri_line.startswith(''):
                flag=False
                print(''*10+'You should add a blank line before this line.')
                line='\n'+line
        if flag:
            print(''* 10+'pass.')
        fp.write(line)
    fp.close()
if __name__=='__main__':
    fileName=sys.argv[1]
    fileLines=[]
    with open(fileName,'r')as fp:
        fileLines=fp.readlines()
    desFileName=fileName[:-3]+'_new.py'
    checkFormats(fileLines,desFileName)
    comments=[line for line in fileLines if line.strip().startswith('#')]
    ratio=len(comments)/len(fileLines)
    if radio <=0.3:
        print('='*30)
        print('comments in the file is les than 30%.')
        print('Perhaps you should add some comments at appropriate position')
                
