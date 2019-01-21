# coding: UTF-8

import os
import sys

from Model import mod_cmake

if __name__ == '__main__':
    import path_init

if len(sys.argv) == 3:
    pathSrc = sys.argv[1].decode('GBK')  #命令行的参数是GBK
    pathDis = sys.argv[2].decode('GBK')  # 命令行的参数是GBK

    if not os.path.exists(pathSrc):
        print u"源代码路径不存在"
    else:
        if not os.path.exists(pathDis):
            print u"目标路径不存在"
        else:
            mod_cmake.doCmkae(pathSrc,pathDis)
else:
    print u"缺少参数"