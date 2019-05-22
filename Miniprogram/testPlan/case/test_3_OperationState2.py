import requests
import unittest
import re
from testPlan.common.commonFun import Fun
from testPlan.common.commonElement import Login_getToken,Url
import json
#加了self，以后，这个变量就变成了全局变量，在类中的其他函数中也可以调用。
#class A:
    #def go(self):
        #self.one= 'sdf'
    #def go1(self):
        #print self.one

#a = A()
#a.go()
#a.go1()

class Function:
    def getStatus(self): #写死getStatus请求
        token = Fun.take_token('../common/token.json')
        print("Get Appliance's Status Interface Test")
        url1 = Url.server + "/api/homeappliances/BOSCH-WTU879H00W-68A40E03C617/status"
        header = {'Content-Type': 'application/json'}
        header1_1 = Fun.merge_Two_Dicts(header, token)
        response1 = requests.get(url=url1, params={}, headers=header1_1)
        return response1

class MyTest(unittest.TestCase):
    response1 = Function().getStatus()  #调用getStatus请求,注意先实例化
    def setUp(self):
        print("start test")
        pass

    def test_1_getStatus(self):
        response1 = self.response1
        d = json.loads(response1.text)
        assert response1.status_code == 200
        assert d["msg"] == "成功", "retInfo not right"
        assert "status" in d["data"].keys()
        print("Get Appliance's Status pass")
        print("response code :" + str(response1.status_code))
        print("r.elapsed.millisecond :" + str(response1.elapsed.microseconds/1000))
        print("response data :" + response1.text)

    def tearDown(self):
        print("end test")
        pass


if __name__=="__main__":
    unittest.main()