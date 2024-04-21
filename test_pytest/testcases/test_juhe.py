# _*_ coding : utf_8 _*_
# @Time : 18:22 
# @Author : 田霄汉
# @File : test_gettoken
# @Project : APIAutoTest
# @User : Administrator
import pytest
from test_pytest.Utils.requestsutils import *
from test_pytest.Utils.operationyaml import *
import os


class TestRole():


    session = requests.session()
    extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
    birthToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../birthToLuck.yml'))
    QQToLuck_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../QQToLuck.yml'))

    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(birthToLuck_file))
    def test_birthToLuck(self, caseinfo):

        # 通过生日看运势
        # params = {
        #     "date": "2014-01-01",
        #     "key": "ef56c560a51857bd1a0e5d394345ea9c"
        # }
        # headers = {
        #     "Content-Type": "application/x-www-form-urlencoded"
        # }
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        result = TestRole().session.request(method=method, url=url, params=data, headers=headers)
        result = result.json()
        print(result)
        # YamlUtils().write_yaml_add(self.extract_file, {"reason01":result["reason"]})
        # result = RequestsUtils().send_request(method='get', url='http://v.juhe.cn/laohuangli/d', data=params, headers=headers)
        # result = json.loads(result)
        # YamlUtils().write_yaml_add(self.extract_file, {"reason01":result["reason"]["yangli"]})
        # YamlUtils().write_yaml_add(self.extract_file, {"wuxing":result["result"]["wuxing"]})
        # assert result["result"]["yangli"] == "2014-01-01"
        # assert result["reason"] == "超过每日可允许请求次数!"

    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(QQToLuck_file))
    def test_QQToLuck(self, caseinfo):

        # 通过QQ号码看运势

        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        # data = {
        #     "qq": "522989570",
        #     "key": "63e04654aed68eb611dc26efc4e53caa"
        # }
        # headers = {
        #     "Content-Type": "application/x-www-form-urlencoded"
        # }
        # result = RequestsUtils().send_request(method='post', url=url, data=data, headers=headers)
        # result = json.loads(result)
        # YamlUtils().write_yaml_add(self.extract_file, {"conclusion":result["result"]["data"]["conclusion"]})
        # assert result["reason"] == "success"
        result = TestRole().session.request(method=method, url=url, data=data, headers=headers)
        result = result.json()
        print(result)
        # YamlUtils().write_yaml_add(self.extract_file, {"reason02":result["reason"]})
        # assert result["reason"] == "请求超过次数限制"
    #
    # def test_readbirthLuck(self, connectDB):
    #
    #     # birthday = info["yangli"]
    #     # wuxing = info["wuxing"]
    #     # print("出生日期为%s的人的五行运势为%s"%(birthday, wuxing))
    #     reason01 = YamlUtils().read_yaml(filename=self.extract_file, keys="reason01")
    #     print("五行运势为%s"%reason01)
    #
    # def test_readQQLuck(self):
    #
    #     # # QQ = info[]
    #     # luck = info["conclusion"]
    #     # print("此QQ号的人的运势为%s"%luck)
    #     reason02 = YamlUtils().read_yaml(filename=self.extract_file, keys="reason02")
    #     print("此QQ号的人的运势为%s"%reason02)
    #
    # @pytest.mark.smoke
    # def test_quit(self):
    #
    #     print("成功退出")

if __name__ == '__main__':
    pytest.main()