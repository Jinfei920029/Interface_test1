from testPlan.common.commonFun import Login_Element,Fun
from testPlan.common.myglobal import *

#token = Fun.take_token('../common/token.json')
#print d.has_key('name')
#print ‘name’ in d.keys()
#print 'name' in d
d = {"retCode":"0001","retInfo":"success","retBody":{"address":"CN|广东|中山|None|OTHER|0|0","content":{"address_detail":{"province":"广东省","city":"中山市","street":"","district":"","street_number":"","city_code":187},"address":"广东省中山市","point":{"x":"12626223.35","y":"2560577.37"}},"status":0}}
assert d["retInfo"] == "success" ,"retInfo not right"
assert "retBody" in d.keys()
