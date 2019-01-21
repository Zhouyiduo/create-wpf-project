# coding: UTF-8
import os

def doCmkae( pathOrg , pathDis ):

    if not os.path.exists(pathOrg):
        print u"源代码路径错误"
        return

    if not os.path.exists(pathDis):
        print u"生成路径错误"
        return

    #切换到盘符
    #pf = pathDis[:2]
    #os.system(pf)

    #切换到工程路径下
    os.chdir(pathOrg)

    #执行CMake命令
    os.system("cmake " + pathDis +  " -G \"Visual Studio 15 2017\"")
    return