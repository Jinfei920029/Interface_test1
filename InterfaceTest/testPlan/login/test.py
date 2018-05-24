from testPlan.common.commonFun import Fun
#save_to_file('mobiles.txt', 'your contents str')
response3 = "jinfei2"
token_info = Fun.re_write(response3)

Fun.save_to_jsonfile('../common/token.json', token_info)

print(token_info)
print(type(token_info))
