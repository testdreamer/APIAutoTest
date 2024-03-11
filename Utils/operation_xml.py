#-- coding: utf-8 --

#@Time : 2022/9/20 15:57

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_xml.py

#@Software: PyCharm
import lxml.etree
def from_xpath_update_content(xml_path,xpath,content):
    """
    根据xpath修改xml内容
    :param xml_path: xml文件路径
    :param xpath: xpath
    :param content: 要修改的内容
    :return:
    """
    root = lxml.etree.parse(xml_path)
    for i in range(0, len(root.xpath(xpath))):
        root.xpath(xpath)[i].text = content
    root.write(xml_path, encoding='utf-8')