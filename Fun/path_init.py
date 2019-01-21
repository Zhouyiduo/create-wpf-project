#coding:utf-8

import sys
import os

print u"工程路径为："
path = os.path.dirname(os.path.realpath(__file__))
pathSecs = str.split(path, u"\\")
pathsys = u""
for index in range(len(pathSecs)):
    if (index == len(pathSecs) - 1):
        break
    else:
        if (index == len(pathSecs) - 2):
            pathsys += pathSecs[index]
        else:
            pathsys += pathSecs[index] + u"\\"
sys.path.append(pathsys)

print u"工程路径为：" +  pathsys

