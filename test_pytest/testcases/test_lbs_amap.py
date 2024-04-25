# _*_ coding : utf_8 _*_
# @Time : 21:06 
# @Author : 田霄汉
# @File : test_lbs_amap
# @Project : APIAutoTest
# @User : Administrator


import pytest
from test_pytest.Utils.requestsutils import *
from test_pytest.Utils.operationyaml import *
from test_pytest.Utils.envreplaceyaml import *
import os


class TestLbsAmap():

    # extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
    # test_weather_forecast_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_weather_forecast.yml'))
    # test_IP_location_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_IP_location.yml'))

    extract_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract.yml'))
    test_IP_location_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_IP_location.yml'))
    test_weather_forecast_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_weather_forecast.yml'))
    old_test_IP_location_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_test_IP_location.yml'))
    old_test_weather_forecast_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_test_weather_forecast.yml'))
    EnvReplaceYaml(old_test_IP_location_file, test_IP_location_file)
    EnvReplaceYaml(old_test_weather_forecast_file, test_weather_forecast_file)


    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(test_weather_forecast_file))
    def test_WeatherForecast(self, caseinfo):

        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        validate = caseinfo["validate"]
        result = RequestsUtils().send_request(method=method, url=url, data=data, headers=headers)
        result = json.loads(result)
        # print(result)
        if "lives" in result:
            if result["lives"][0]:
                if result["lives"][0]["city"] == "东城区":
                    YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"weather_city":result["lives"][0]["city"]})
                    YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"weather_adcode": result["lives"][0]["adcode"]})
                    assert result["info"] == validate
                else:
                    assert result["info"] == validate
            else:
                assert result["info"] == validate
        else:
            assert result["info"] == validate


    @pytest.mark.parametrize("caseinfo", YamlUtils().read_yaml_no_key(test_IP_location_file))
    def test_IPLocation(self, caseinfo):

        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        validate = caseinfo["validate"]
        result = RequestsUtils().send_request(method=method, url=url, data=data, headers=headers)
        result = json.loads(result)
        if "city" in result:
            if result["city"]:
                if result["city"] == "北京市":
                    YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"IP_city": result["city"]})
                    YamlUtils().write_yaml_add(dataurl=self.extract_file, content={"IP_adcode": result["adcode"]})
                    assert result["info"] == validate
                else:
                    assert result["info"] == validate
            else:
                assert result["info"] == validate
        else:
            assert result["info"] == validate


    def test_verify_WeatherForecast(self, connectDB):

        weather_province = YamlUtils().read_yaml(filename=self.extract_file, keys="weather_province")
        weather_adcode = YamlUtils().read_yaml(filename=self.extract_file, keys="weather_adcode")
        print(weather_province)
        print(weather_adcode)


    def test_verify_IPLocation(self):

        IP_province = YamlUtils().read_yaml(filename=self.extract_file, keys="IP_province")
        IP_adcode = YamlUtils().read_yaml(filename=self.extract_file, keys="IP_adcode")
        print(IP_province)
        print(IP_adcode)