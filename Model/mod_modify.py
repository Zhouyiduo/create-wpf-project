
#coding:utf-8
import os
import codecs




# 定义一个函数，带有4个参数
# x 表示要更新的文件名称
# y 表示要被替换的内容
# z 表示 替换后的内容
# s 默认参数为 1 表示只替换第一个匹配到的字符串
# 如果参数为 s = 'g' 则表示全文替换
def string_switch(fileName,oldStr,newStr):
    f = codecs.open(fileName, "r" ,"utf-8")
    lines = f.readlines()

    f_w = codecs.open(fileName, "w","utf-8")
    for line in lines:
        if oldStr in line:
            line = line.replace(oldStr, newStr)
        f_w.write(line)
    return True


def dir_switch(dirName,oldStr,newStr):

    for fileName in os.listdir(dirName):

        absourcePath = os.path.join(dirName, fileName)

        if os.path.isdir(absourcePath):
            # 递归调用getDirAndCopyFile()函数
            if dir_switch(absourcePath, oldStr,newStr) == False:
                return  False

        if os.path.isfile(absourcePath):
            #替换字符
            if string_switch(absourcePath, oldStr, newStr) == False:
                return  False
    return True