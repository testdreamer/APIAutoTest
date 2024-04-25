# _*_ coding : utf_8 _*_
# @Time : 18:22 
# @Author : 田霄汉
# @File : test_gettoken
# @Project : APIAutoTest
# @User : Administrator
import pytest
import requests

from test_pytest.Utils.requestsutils import *
from test_pytest.Utils.operationyaml import *
import os
from test_pytest.Utils.envreplaceyaml import *


class TestClass():

    extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
    birthToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../birthToLuck.yml'))
    QQToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../QQToLuck.yml'))
    old_birthToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_birthToLuck.yml'))
    old_QQToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_QQToLuck.yml'))
    EnvReplaceYaml(old_birthToLuck_file, birthToLuck_file)
    EnvReplaceYaml(old_QQToLuck_file, QQToLuck_file)



    # extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
    # birthToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../birthToLuck.yml'))
    # QQToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../QQToLuck.yml'))

    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(birthToLuck_file))
    def test_birthToLuck(self, caseinfo):


        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        validate = caseinfo["validate"]

        result = RequestsUtils().send_request(method=method, url=url, data=data, headers=headers)
        result = json.loads(result)

        # 写入关联文件extract.yml
        extract = YamlUtils().read_yaml_no_key(filename = self.extract_file)
        while "yangli" not in str(extract):
            YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"yangli": result["result"]["yangli"]})
            YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"wuxing": result["result"]["wuxing"]})
            # YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"content":"test"})
            # YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"content":"test"})
            break

        # 进行断言
        if result["result"] == None:
            assert str(result["result"]) == validate
        else:
            assert result["result"] == validate

    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(QQToLuck_file))
    def test_QQToLuck(self, caseinfo):

        # 通过QQ号码看运势

        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        validate = caseinfo["validate"]

        result = RequestsUtils().send_request(method=method, url=url, data=data, headers=headers)
        result = json.loads(result)
        # print(result)

        # 写入关联文件extract.yml
        extract = YamlUtils().read_yaml_no_key(filename=self.extract_file)
        if "conclusion" not in str(extract):
            YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"conclusion":result["result"]["data"]["conclusion"]})
            # YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"content":"test"})
        else:
            pass

        # 进行断言
        if "result" in result:
            if result["result"] == None:
                assert str(result["result"]) == validate
            else:
                assert result["result"] == validate
        else:
            assert result["status"] == 404
        # assert result["reason"] == "请求超过次数限制"

    def test_readbirthLuck(self, connectDB):

        yangli = YamlUtils().read_yaml(filename=self.extract_file, keys="yangli")
        wuxing = YamlUtils().read_yaml(filename=self.extract_file, keys="wuxing")
        print("阳历%s五行运势为%s"%(yangli, wuxing))

    def test_readQQLuck(self):

        conclusion = YamlUtils().read_yaml(filename=self.extract_file, keys="conclusion")
        print("此QQ号的人的运势为%s"%conclusion)

    @pytest.mark.smoke
    def test_quit(self):

        print("成功退出")