import re

class Fun:
    #定义函数jsonFile用来保存获取的response到指定文件
    def jsonFile(fileData):
        file = open("C:\Software\pycharm\json.txt", "w")
        file.write(fileData)
        print("Data  OK")
        file.close()
    #定义函数getSession用来获取返回的sessionid和sessiondate
    def getSessionId(response):
        # 正则表达式截取返回结果的SessionID格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        res = r'<input type="hidden" name="sessionId" value="(.*?)"/>'
        m = re.findall(res, response, re.S | re.M)
        sessionid = str(m[0])
        return sessionid
    def getSessionData(response):
        # 正则表达式截取返回结果的SessionData格式：res = r'<td>(.*?)</td><td>(.*?)</td>'
        res = r'<input type="hidden" name="sessionData" value="(.*?)"/>'
        m = re.findall(res, response, re.S | re.M)
        sessiondata = str(m[0])
        return sessiondata
    #两个字典类型合并的函数
    def merge_Two_Dicts(x,y):
        z = x.copy()
        z.update(y)
        return z
class Login_Element:
    server1 = "https://api.home-connect.cn"
    server2 = "https://solution.home-connect.cn"
    login_url1 = server1+"/security/oauth/authorize"
    login_url2 = server1+"/security/oauth/login"
    login_url3 = server2+"/sfmapi/getAuthToken"
    params1 = {'response_type': 'code',
               'client_id': '970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07'}
    header2 = {"Content-Type": "application/x-www-form-urlencoded",
               "client_id": "970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07"}
    header3 = {'Content-Type': 'application/x-www-form-urlencoded',
               'ha_id': 'SIEMENS-KA92NP49TI-68A40E005BA3',
               'device_code': '123456789'}
    message2 = {"client_id": "970F224CEB3BC18966E2A0564D00B88235FCB2753FCC9C98C1208199EF651F07",
                "email": "pcn80507@grr.la",
                "password": "qwer-1234",
                }