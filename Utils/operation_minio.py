#-- coding: utf-8 --

#@Time : 2022/11/15 11:10

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_minio.py

#@Software: PyCharm
#MinIO Browser是一个文件共享容器
import minio
import traceback
import oss2
from minio import Minio
from minio.error import S3Error

def minio_file_upload(end_point: str, access_key: str, secret_key: str, bucket: str, remote_path: str, local_path: str):
    """
    向minio上传文件
    :param end_point: 服务器地址
    :param access_key: minio用户名
    :param secret_key:minio密码
    :param bucket:桶名
    :param remote_path:文件在桶里的路径
    :param local_path:本地文件路径
    :return:
    """
    try:
        _end_point = end_point.replace('https://', '').replace('http://', '')
        # Create a client with the MinIO server playground, its access key
        # and secret key.
        client = Minio(
            _end_point,
            access_key=access_key,
            secret_key=secret_key,
            secure=False
        )

        # Make 'asiatrip' bucket if not exist.
        found = client.bucket_exists(bucket)
        if not found:
            client.make_bucket(bucket)
        else:
            print("Bucket {} already exists".format(bucket))

        # Upload '/home/user/Photos/asiaphotos.zip' as object name
        # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
        client.fput_object(
            bucket, remote_path, local_path,
        )
        print(
            "{} is successfully uploaded as "
            "object {} to bucket {}.".format(local_path, remote_path, bucket)
        )
    except S3Error as e:
        print(
            "*** minio上传文件异常 -> {} {}".format(str(e), traceback.format_exc()))
        raise Exception("minio上传文件异常:[{}]".format(str(e)))


def oss_file_upload(end_point: str, access_key: str, secret_key: str, bucket: str, remote_path: str, local_path: str):
    """
    oss文件上传minio
    :param end_point: 服务器地址
    :param access_key: minio用户名
    :param secret_key:minio密码
    :param bucket:桶名
    :param remote_path:文件在桶里的路径
    :param local_path:本地文件路径
    :return:
    """
    try:
        _end_point = end_point.replace('https://', '').replace('http://', '')
        # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
        auth = oss2.Auth(access_key, secret_key)
        # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        # 填写Bucket名称。
        bucket = oss2.Bucket(auth, _end_point, bucket)

        # 填写Object完整路径和本地文件的完整路径。Object完整路径中不能包含Bucket名称。
        # 如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        bucket.put_object_from_file(remote_path, local_path)
    except S3Error as e:
        print(
            "*** oss上传文件异常 -> {} {}".format(str(e), traceback.format_exc()))
        raise Exception("oss上传文件异常:[{}]".format(str(e)))


import logging
from minio import Minio
from minio.error import S3Error

logging.basicConfig(
    level=logging.INFO,
    filename='../mysqlbackup_downlaod.log',
    filemode='a',
    format='%(asctime)s %(name)s %(levelname)s--%(message)s'
)

file_name = "mysql_monitor.py"
file_path = "C:\\Users\\lpy\\Desktop\\img\\{}".format(file_name)


def download_file():
    """
    Python实现Minio的下载（主要用于异地备份的中转站）
    :return:
    """
    # 创建一个客户端
    minioClient = Minio(
        'minio.***.com',
        access_key='admin',
        secret_key='****',
        secure=False
    )
    try:
        minioClient.fget_object(
            bucket_name="backup",
            object_name="mysql/dev/{}".format(file_name),
            file_path=file_path
        )
        logging.info("file '{0}' is successfully download".format(file_name))
    except S3Error as err:
        logging.error("download_failed:", err)


# minio_conf = {
#     'endpoint': '192.168.13.148:63805',
#     'access_key': 'AKIAIOSFODNN7EXAMPLE',
#     'secret_key': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
#     'secure': False
# }
#
# def up_data_minio(bucket: str):
#     """
#     向minio上传文件
#     :param bucket:文件名
#     :return:
#     """
#     client = minio.Minio(**minio_conf)
#     client.fput_object(bucket_name=bucket, object_name='test2',
#                        file_path='test.zip',
#                        content_type='application/zip'
#                        )
#
#
# def load_data_minio(bucket: str):
#     """
#     从minio下载文件
#     :param bucket:文件名
#     :return:
#     """
#     client = minio.Minio(**minio_conf)
#     if not client.bucket_exists(bucket):
#         return None
#     data = client.get_object(bucket, 'test2')
#     path = "receive.zip"
#     with open(path, 'wb') as file_data:
#         for d in data.stream(32 * 1024):
#             file_data.write(d)
#     return data.data
#
#

