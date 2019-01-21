#coding:utf-8

import os

"""
利用递归实现目录的遍历
@para  sourcePath:原文件目录
@para  targetPath:目标文件目录
"""
def getDirAndCopyFile(sourcePath, targetPath):
   if not os.path.exists(sourcePath):
        print u"源代码路径不存在"
        return False
   if not os.path.exists(targetPath):
        mkdir_recursively(targetPath)
      #os.makedirs(targetPath)

   if os.listdir(targetPath):
      print u"目标目录不为空"
      return False

   # 遍历文件夹
   for fileName in os.listdir(sourcePath):
      # 拼接原文件或者文件夹的绝对路径
      absourcePath = os.path.join(sourcePath, fileName)
      # 拼接目标文件或者文件加的绝对路径
      abstargetPath = os.path.join(targetPath, fileName)
      # 判断原文件的绝对路径是目录还是文件
      if os.path.isdir(absourcePath):
         # 是目录就创建相应的目标目录
         os.makedirs(abstargetPath)
         # 递归调用getDirAndCopyFile()函数
         getDirAndCopyFile(absourcePath, abstargetPath)
      # 是文件就进行复制
      if os.path.isfile(absourcePath):
         rbf = open(absourcePath, "rb")
         wbf = open(abstargetPath, "wb")
         while True:
            content = rbf.readline(1024 * 1024)
            if len(content) == 0:
               break
            wbf.write(content)
            wbf.flush()
         rbf.close()
         wbf.close()


def mkdir_recursively(path):
   local_path = path.replace(u'\\', '/')

   path_list = local_path.split('/')
   print path_list

   if path_list is None: return False

   # For windows, we should add the '\\' at the end of disk name. e.g. C: -> C:\\
   disk_name = path_list[0]
   if disk_name[-1] == ':': path_list[0] = path_list[0] + '\\'

   dir = ''
   for path_item in path_list:
      dir = os.path.join(dir, path_item)
      print u"dir:", dir
      if os.path.exists(dir):
         if os.path.isdir(dir):
            print u"mkdir skipped: %s, already exist." % (dir,)
         else:  # Maybe a regular file, symlink, etc.
            print u"Invalid directory already exist:", dir
            return False
      else:
         try:
            os.mkdir(dir)
         except Exception, e:
            print "mkdir error: ", dir
            print e
            return False
         print "mkdir ok:", dir
   return True