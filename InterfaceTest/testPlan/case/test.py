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


url = BasicSupport_Element.IPLocation_url
data = {}
head = Fun.merge_Two_Dicts(BasicSupport_Element.header1,token)
head2 = {'Content-Type': 'application/json','bshtoken': 'eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJzdWIiOiIxMjMiLCJoYV9pZCI6IlNJRU1FTlMtS0E5Mk5QNDlUSS02OEE0MEUwMDVCQTMiLCJkZXZpY2VfY29kZSI6IjEyMzQ1Njc4OSIsImVtYWlsIjoicGNuOTBAZ3JyLmxhIn0.qyn_2zdatoqOYJUhBdJdjjZvqkv6w0aPLncNsMwg85WjGpm2JhT5_5t9IQYhSKjhVIjpb8Qegnt-4UtIiFDTaQ'}
response = Fun.post_url(url,data={},headers = head)