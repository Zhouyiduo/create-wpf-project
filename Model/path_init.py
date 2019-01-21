#coding:utf-8

import sys
import os
#print u"不设置工程路径"
if __name__ == '__main__':
    print u"不设置工程路径"
else:
    #print u"工程路径为："

    #os.system(u"chcp 65001")
    #os.system(u"chcp 963")
    path = os.path.dirname(os.path.realpath(__file__));
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
    print u"工程路径为：" + pathsys