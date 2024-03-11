#-- coding: utf-8 --

#@Time : 2022/7/28 18:21

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_remote_server.py

#@Software: PyCharm
import paramiko
from Utils.operationini import *
cf = Conf

def file_download_linux(hostname,username,password,file_original, file_aim):
    """
    远程服务器上的文件下载到本地
    :param hostname: 服务器地址
    :param username: 服务器用户名
    :param password: 服务器密码
    :param file_original: 远程文件源
    :param file_aim: 本地文件源
    :return:
    """
    # linux服务器信息
    host_ip = hostname
    host_username = username
    host_password = password

    t = paramiko.Transport((host_ip, 22))
    t.connect(username=host_username, password=host_password)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 下载操作
    try:
        sftp.get(file_original, file_aim)
    except OSError:
        print('got OSError')
    finally:
        sftp.close()

def file_upload_linux(hostname,username,password,file_aim,file_original ):
    """
    本地文件上传到远程服务器
    :param hostname: 服务器地址
    :param username: 服务器用户名
    :param password: 服务器密码
    :param file_original: 远程文件源
    :param file_aim: 本地文件源
    :return:
    """
    # linux服务器信息
    host_ip = hostname
    host_username = username
    host_password = password

    t = paramiko.Transport((host_ip, 22))
    t.connect(username=host_username, password=host_password)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 下载操作
    try:
        sftp.put(file_aim,file_original)
    except OSError:
        print('got OSError')
    finally:
        sftp.close()

def execute_linux_commnd(hostname,username,password,commnd):
    """
    远程执行linux命令
    :param hostname:服务器地址
    :param username:服务器用户名
    :param password:服务器密码
    :param commnd:执行的linux命令(如果是非linux&shell命令,只能在命令执行前增加source /etc/profile,如果是连续的命令,中间用;隔开)
    :return:
    """

    #创建ssh对象
    ssh = paramiko.SSHClient()
    #允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接服务器
    ssh.connect(hostname=hostname,port=22,username=username,password=password)
    #执行命令
    stdin,stdout,stderr = ssh.exec_command(commnd)

    #获取命令结果
    result = stdout.read()
    #将types转为str
    result = result.decode('gbk')
    print(result)
    ssh.close()