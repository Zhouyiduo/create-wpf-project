#coding:utf-8
import sys

from Model import mod_modify

if __name__ == '__main__':
    import path_init

if len(sys.argv) == 2:
    pathReplace = sys.argv[1].decode('GBK')       #命令行的参数是GBK
    mod_modify.dir_switch("D:\python_project","{Example}","DemoEx1")
    print u"修改完成"
else:
    print u"缺少参数"








