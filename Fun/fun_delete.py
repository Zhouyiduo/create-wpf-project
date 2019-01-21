# coding: UTF-8
import os
import sys

from Model import mod_delete

if __name__ == '__main__':
    import path_init


if len(sys.argv) == 2:
    pathDel = sys.argv[1].decode('GBK')       #命令行的参数是GBK
    if not os.path.exists(pathDel):
        print u"删除的路径不存在"
    else:
        mod_delete.deleteDir(pathDel)
else:
    print u"缺少参数"
