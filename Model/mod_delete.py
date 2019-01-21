# coding: UTF-8

import shutil

#os.removedirs(path)  # 递归地删除目录。如果子目录成功被删除，则将会成功删除父目录，子目录没成功删除，将抛异常。

def deleteDir( path ):
    shutil.rmtree(path)