#!usr/bin/python
#conding=utf-8
import sys
import zlib
import os.path
filename=sys.argv[1]
if os.path.isfile(filename):
    fp=open(filename,'rb')
    content=fp.read()
    fp.close()
    print(zlib.crc32(contents.encode()))
else:
    print('file not exists')
print('检测文件的循环冗余')    
