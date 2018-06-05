import requests
import unittest
from testPlan.common.commonFun import BasicSupport_Element,Fun
import json
token = Fun.take_token('../common/token.json')

#def get_url(url, params ,headers):
# url = url
# params = params
# headers = headers
# response = requests.get(url = url , params = params,headers= headers)
# d = json.loads(response.text)
# assert response.status_code == 200
# assert d["retInfo"] == "success", "retInfo not right"
# assert "retBody" in d.keys()
# print("status_code_IPLocation:" + str(response.status_code))
# print(response.text)
#  print("pass")

def post_url(url, data, headers):
    url = url
    data = data
    headers = headers
    response = requests.post(url=url, data=data, headers=headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d["retInfo"] == "success", "retInfo not right"
    assert "retBody" in d.keys()
    print("status_code_IPLocation:" + str(response.status_code))
    print(response.text)
    print("pass")


url = BasicSupport_Element.Realtimeweather_url
params = {}
head = Fun.merge_Two_Dicts(BasicSupport_Element.header2, token)
Fun.get_url(url,params,head)
