#coding:utf-8

import sys
import os


from Model import mod_copy
from Model import mod_modify
from Model import mod_cmake

sourcePath = u"../template"
if len(sys.argv) == 3:

    print u"开始创建工程"
    projectPath = sys.argv[1].decode('GBK')
    projectName = sys.argv[2].decode('GBK')

    targetPath = projectPath + u"/" + projectName
    if  mod_copy.getDirAndCopyFile(sourcePath, targetPath) == False :
        print u"创建失败: 拷贝失败！"
        exit()
    if mod_modify.dir_switch(projectPath,u'{Example}',projectName) == False :
        print u"创建失败: 修改失败！"
        exit()
    if mod_cmake.doCmkae(targetPath ,u'./') == False:  #生成到同一个文件夹下
        print u"创建失败: CMake执行失败！"
        exit()
    print u"创建工程完毕"

else:
    print u"缺少参数"