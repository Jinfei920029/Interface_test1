
import json
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

def re_write(response1):
    user_info = '{\"name\" : \"' + response1 + '\"}'
    return user_info

#save_to_file('mobiles.txt', 'your contents str')
name = "jinfei2"
user_info = re_write(name)
print(user_info)
print(type(user_info))
save_to_file('token.json',user_info)