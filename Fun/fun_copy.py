#coding:utf-8

import time
from Model import mod_copy

if __name__ == '__main__':
    import path_init

if __name__ == '__main__':
   startTime = time.clock()
   sourcePath = ur"../template"
   targetPath = ur"D:/python_project/template_new"
   mod_copy.getDirAndCopyFile(sourcePath, targetPath)
   # 时间是用来计算复制总共消耗了多少时间
   endTime = time.clock()
   time_mi = endTime // 60
   time_s = endTime // 1 % 60
   time_ms = ((endTime * 100) // 1) % 100
   print("总用时:%02.0f:%02.0f:%2.0f" % (time_mi, time_s, time_ms))
