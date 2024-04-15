import zipfile
import os
# from Utils.zip_file import make_zip

source_filename = os.path.dirname(__file__)+'/data/test_zip'
out_filename = os.path.dirname(__file__)+'/data/test_zip.zip'

# 创建zip文件，并以写入的方式打开out_filename
zipf = zipfile.ZipFile(file=out_filename, mode='w')
# 获取source_filename的父路径的长度
len_dir = len(os.path.dirname(source_filename))

# 遍历source_filename及其子目录的根目录，子目录，子文件
for father, dirnames, filenames in os.walk(source_filename):
    # 遍历filenames列表，获取每个子文件
    for filename in filenames:
        # 通过上面的遍历，拼接得到每个子文件的绝对路径
        filepath = os.path.join(father, filename)
        # 截取绝对路径后面的部分，获取所有子文件的相对路径，os.path.sep是匹配不同平台路径分隔符，windows是"\",linux是"/"
        arcname = filepath[len_dir:].strip(os.path.sep)  # 相对路径
        # 将source_filename中的全部子文件的绝对路径和相对路径写入到out_filename
        zipf.write(filepath, arcname)
zipf.close()