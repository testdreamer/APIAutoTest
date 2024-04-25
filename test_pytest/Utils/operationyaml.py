#-- coding: utf-8 --#@Time : 2022/5/9 14:16#@Author : tianxh#@Email : 729560832@qq.com#@File : operationyaml.py#@Software: PyCharmimport jsonimport sys,ossys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))from ruamel import yamlimport wget# import yamlclass YamlUtils:    def write_yaml(self, dataurl, content):        """        写yaml文件        :param dataurl: yaml文件路径        :param content: 要写入的内容,dict类型        :return:        """        with open(dataurl, 'w', encoding='utf-8') as f:            # 将字典写入到yaml文件中            yaml.dump(content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)            # f.close()    def write_yaml_add(self, dataurl, content):        """        以追加的方式写yaml文件        :param dataurl: yaml文件路径        :param content: 要写入的内容,dict类型        :return:        """        with open(dataurl, 'a', encoding='utf-8') as f:            # 将字典写入到yaml文件中            yaml.dump(content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)            # f.close()    """    读取有key的yaml文件    filename为yaml文件名    keys为键值    """    def read_yaml(self, filename, keys):        with open(filename, 'r', encoding="utf-8") as f:            # yaml文件中读取内容            msg = yaml.load(f, Loader=yaml.Loader)            return msg.get(keys)    """    读取没有key的yaml文件    filename为yaml文件名    """    def read_yaml_no_key(self, filename):        with open(filename, 'r', encoding="utf-8") as f:            # yaml文件中读取内容            msg = yaml.load(f, Loader=yaml.Loader)            return msg    def clear_yaml(self, filename):        """        清除yaml文件内容        :param filename:        :return:        """        with open(filename, mode='w', encoding='utf-8') as f:            f.truncate()            f.close()    def from_wget_download_file(self, filename, original_file):        """        用wget方式下载文件        :param filename: 文件源地址        :param original_file: 重命名的路径及名称        :return:        """        if os.path.exists(original_file):            os.remove(original_file)        else:            print("The file does not exist")        # 下载文件，重新命名输出文件名        file_name = wget.download(filename, out=original_file)        print(file_name)