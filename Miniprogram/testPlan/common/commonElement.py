import re
import json
import sys
import requests

sys.path
class Url:
    server = "https://solution.home-connect.cn"

class Login_getToken:
    server = "https://solution.home-connect.cn"
    login_url = server + "/api/v1/wx/account/backdoor/login"
    header = {'Content-Type':'application/json'}
    body = {"loginId":"+8617625933090","password":"qwer1234.",
            "deviceId":"606720403ABEOvenMasterFA58F3C16CC28DA8","tokenLifetime":"permanent",
            "openid":"eyJ4LWVudiI6IlZBTCIsImFs3090"}