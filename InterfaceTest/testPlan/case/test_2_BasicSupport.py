import requests
import unittest
from testPlan.common.commonFun import BasicSupport_Element,Fun
import json

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("-----start test Basic Support-----")
        pass

    def test_01_IPLocationInterface(self):
        print("IP Location Interface Test")
        token = self.token
        self.url1 = BasicSupport_Element.IPLocation_url
        head1_1 = Fun.merge_Two_Dicts(BasicSupport_Element.header1, token)
        Fun.post_url(self.url1, data={}, headers=head1_1)

    def test_02_Realtimeweather(self):
        print("Real time weather Interface Test")
        token = self.token
        self.url2 = BasicSupport_Element.Realtimeweather_url
        heaad2_2 = Fun.merge_Two_Dicts(BasicSupport_Element.header2, token)
        response2 = requests.get(url=self.url2, params={},headers=heaad2_2)
        d = json.loads(response2.text)
        assert response2.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response2.status_code))
        print("pass")

    def test_03_WeatherforecastInterface(self):
        print("Weather forecast Interface Test")
        token = self.token
        self.url3 = BasicSupport_Element.WeatherforecastInterface_url
        heaad3_3 = Fun.merge_Two_Dicts(BasicSupport_Element.header3, token)
        response3 = requests.get(url=self.url3, params={}, headers=heaad3_3)
        d = json.loads(response3.text)
        assert response3.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response3.status_code))
        print("pass")

    def test_04_TimeSynchronizationInterface(self):
        print("Time Synchronization Interface Test")
        token = self.token
        self.url4 = BasicSupport_Element.TimeSynchronization_url
        self.params = {}
        self.head4_4 = Fun.merge_Two_Dicts(BasicSupport_Element.header4, self.token)
        Fun.get_url(self.url4, self.params,self.head4_4 )
    def tearDown(self):
        print("-----end test Basic Support-----")
        pass
if __name__=="__main__":
    unittest.main()