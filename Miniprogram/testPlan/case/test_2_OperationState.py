import requests
import unittest
import re
from testPlan.common.commonFun import Fun
from testPlan.common.commonElement import Login_getToken,Url
import json


class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("start test")
        pass

    def test_1_getStatus(self):
        token = self.token
        print("Get Appliance's Status Interface Test")
        self.url1 = Url.server + "/api/homeappliances/BOSCH-WTU879H00W-68A40E03C617/status"
        header = {'Content-Type': 'application/json'}
        header1_1 = Fun.merge_Two_Dicts(header, token)
        response1 = requests.get(url=self.url1, params={}, headers=header1_1)
        d = json.loads(response1.text)
        assert response1.status_code == 200
        print("pass")
        print(response1.text)
    def tearDown(self):
        print("end test")
        pass


if __name__=="__main__":
    unittest.main()