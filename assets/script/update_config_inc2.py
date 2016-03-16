#!/usr/bin/env python
# coding: utf-8

import os
import sys
import shutil

from incrementalConfig_pb2 import incrementResponse


def get_version(file_name):
    try:
        with open(file_name, 'rb') as f:
            increment_response = incrementResponse()
            increment_response.ParseFromString(f.read())
            return increment_response.config_version
    except IOError:
        return 1
    return 1


def rsync_send(dir, filename):

   version = get_version(filename)
   print "version:", version

   print os.path.abspath(filename)
   new_config_file = os.path.abspath("../config/config_inc_%d" %version)
   result_file_name = "config_inc_%d" %version
   
   rsync_key_file = os.path.abspath("rsync_key")
   print "rsync_key_file:", rsync_key_file
   
   shutil.copyfile(os.path.abspath(filename),new_config_file)

   print "new_config_file:", new_config_file

   os.chdir("cwRsync") 
   print os.getcwd()
   command = 'rsync -av --chmod u+rwx -e \"ssh -i c:\\rsync_key" /cygdrive/"'+new_config_file+'" sandbox@113.31.129.172:~/xydldassets/'+config_inc_dir+'/'+result_file_name+''
   print command
   os.system(command)

if __name__ == '__main__':
   config_inc_dir = sys.argv[1]            # 放置增量配置文件的目录
   file_name = "../config/config_inc"      # 增量文件，都是生成到 win32 的 config 下
   rsync_send(config_inc_dir, file_name)
   command = 'rsync -av --chmod u+rwx -e \"ssh -i c:\\rsync_key" /cygdrive/‘’ sandbox@113.31.129.172:~/xydldassets/'+config_inc_dir+''
