import requests
import unittest
from testPlan.common.commonFun import BasicSupport_Element,Fun
import json

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("-----start test Basic Support-----")
        pass

    def test_1_IPLocationInterface(self):
        print("IP Location Interface Test")
        token = self.token
        try:
            self.url1 = BasicSupport_Element.IPLocation_url
            heaad1_1 = Fun.merge_Two_Dicts(BasicSupport_Element.header1, token)
            response1 = requests.post(url=self.url1, data={}, headers=heaad1_1)
            d = json.loads(response1.text)
            assert response1.status_code == 200
            assert d["retInfo"] == "success", "retInfo not right"
            assert "retBody" in d.keys()
        except Exception as e:
            print('Exception', e)
        else:
            print("status_code_IPLocation:" + str(response1.status_code))
            print("pass")

    def test_2_Realtimeweather(self):
        print("Real time weather Interface Test")
        token = self.token
        try:
            self.url2 = BasicSupport_Element.Realtimeweather_url
            heaad2_2 = Fun.merge_Two_Dicts(BasicSupport_Element.header2, token)
            response2 = requests.post(url=self.url2, data={}, headers=heaad2_2)
            d = json.loads(response2.text)
            assert response2.status_code == 200
            assert d["retInfo"] == "success", "retInfo not right"
            assert "retBody" in d.keys()
        except Exception as e:
            print('Exception', e)
        else:
            print("status_code_IPLocation:" + str(response2.status_code))
            print("pass")
    def tearDown(self):
        print("-----end test Basic Support-----")
        pass
if __name__=="__main__":
    unittest.main()