#!/usr/bin/env python
# coding: utf-8

from incrementalConfig_pb2 import incrementResponse

def get_version( file_name ):
    try:
        with open( file_name, 'rb' ) as f:
            increment_response = incrementResponse()
            increment_response.ParseFromString( f.read() )
            return increment_response.config_version
    except IOError:
        return 1

    return 1

##################################################################################
from ftplib import FTP

HOST = "113.31.129.6"
USER = "sandbox"
PASS = "ODk0Y2FmYzllOG"

if __name__ == '__main__':
    config_inc_dir = sys.argv[1]            # 放置增量配置文件的目录

    file_name = "../config/config_inc"      # 增量文件，都是生成到 win32 的 config 下
    config_version = get_version( file_name )

    ftp = FTP( HOST )
    ftp.login( user=USER, passwd=PASS )
    ftp.cwd( config_inc_dir )  # change dir 所有的增量文件，都放在相同的目录里面
    fp = open( file_name )
    ftp.storbinary( "STOR config_inc_%d" % config_version, fp )
