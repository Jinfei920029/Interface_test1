import requests
import unittest
from testPlan.common.commonFun import Login_Element,Fun

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    def setUp(self):
        print("start test")
        pass


    def test_Login1(self):
        #开始第一个get请求获取sessionid和sessiondata
        try:
            self.url1 = Login_Element.login_url1
            params1 = Login_Element.params1
            self.params1 = params1
            response1 = requests.get(url=self.url1, params=self.params1)
        except Exception as e1:
            print('Exception: ', e1)
        else:
            print("status_code1:" + str(response1.status_code))
            sessionid = Fun.getSessionId(response1.text)
            self.sessionid = sessionid
            sessiondata = Fun.getSessionData(response1.text)
            self.sessiondata = sessiondata

        #开始第二个post请求
        try:
            self.url2 = Login_Element.login_url2
            message2 = {"sessionId": sessionid, "sessionData": sessiondata}
            message2_2 = Fun.merge_Two_Dicts(Login_Element.message2, message2)
            header2 = Login_Element.header2
            response2 = requests.post(url=self.url2, data=message2_2, headers=header2)
        except Exception as e2:
            print('Exception',e2)
        else:
            print("status_code2:" + str(response2.status_code))
        #获取token请求

        try:
            self.url3 = Login_Element.login_url3
            message3 = {"sessionId": sessionid}
            header3 = Login_Element.header3
            response3 = requests.post(url=self.url3, data=message3, headers=header3)
        except Exception as e3:
            print('Exception', e3)
        else:
            print("status_code3:" + str(response3.status_code))
            print("token:" + response3.text)
            token_info = Fun.re_write(response3.text)
            Fun.save_to_jsonfile('../common/token.json', token_info)


    def tearDown(self):
        print("end test")
        pass


if __name__=="__main__":
    unittest.main()