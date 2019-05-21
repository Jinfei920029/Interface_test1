import re
import json
import sys
import requests

sys.path
class Fun:
    #定义get函数
    def get_url(url, params, headers):
        url = url
        params = params
        headers = headers
        response = requests.get(url=url, params=params, headers=headers)
        d = json.loads(response.text)
        print(response.text)
        assert response.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response.status_code))
        print("pass")

    # 定义post函数
    def post_url(url, data, headers):
        url = url
        data = data
        headers = headers
        response = requests.post(url, data, headers = headers)
        d = json.loads(response.text)
        print(response.text)
        assert response.status_code == 200
        assert d["retInfo"] == "success", "retInfo not right"
        assert "retBody" in d.keys()
        print("status_code_IPLocation:" + str(response.status_code))
        print("pass")

    # response数据重写
    def re_write(response1):
        user_info = '{\"token\" : \"' + response1 + '\"}'
        return user_info

    #读取文件内容
    def take_token(path):
        with open(path, 'r',encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            return load_dict
            print(load_dict)
    #定义函数jsonFile用来保存获取的response到指定文件
    def save_to_jsonfile(file_name, contents):
        try:
            fh = open(file_name, 'w')
            fh.write(contents)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("内容写入文件成功")
            fh.close()
    #两个字典类型合并的函数
    def merge_Two_Dicts(x,y):
        z = x.copy()
        z.update(y)
        return z