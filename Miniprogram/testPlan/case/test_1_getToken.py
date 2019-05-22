import requests
import re
import unittest
from testPlan.common.commonFun import Fun
from testPlan.common.commonElement import Login_getToken
import json


class MyTest(unittest.TestCase):        #封装测试环境的初始化
    def setUp(self):
        print("start test")
        pass

    def test_1_getToken(self):
        print("get Token")
        url1 = self.url1 = Login_getToken.login_url
        header1 = Login_getToken.header
        body1 = Login_getToken.body
        data1_1 = json.dumps(body1)
        #进行post请求
        r = requests.post(url=self.url1, data=data1_1, headers=header1)
        #获取token值
        response = r.json()
        token = str(response["data"])
        #将字符串里的单引号替换成双引号
        token = re.sub('\'', '\"', token)
        token = re.sub('accessToken', 'Authorization', token)
        #保存到文件token.json
        Fun.save_to_jsonfile('../common/token.json', token)
        print("status_code:" + str(r.status_code))
        print("response:" + str(r.text))

    def tearDown(self):
        print("end test")
        pass


if __name__=="__main__":
    unittest.main()