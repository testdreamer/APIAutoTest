# _*_ coding : utf_8 _*_
# @Time : 20:58 
# @Author : 田霄汉
# @File : test_requests
# @Project : APIAutoTest
# @User : Administrator


import json
from test_pytest.Utils.requestsutils import RequestsUtils
from test_pytest.Utils.operationyaml import *

url = "http://japi.juhe.cn/qqevaluate/qq"
data = {
    "qq": "522989570",
    "key": "63e04654aed68eb611dc26efc4e53caa"
}
json_params = json.dumps(data)
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    # "Content-Type": "application/json"
}
# headers = None
res = RequestsUtils().send_request(method='post', url=url, data=data, headers=headers)
result = json.loads(res)
# extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_pytest/extract.yml'))
# YamlUtils().write_yaml(extract_file, {"conclusion":result['result']['data']['conclusion']})
print(result)