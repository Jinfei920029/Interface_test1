# -*- coding:utf-8 -*-
# Author:Jin Fei
data = {
    '北京':{
        '朝阳':{
            '国贸':{},
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五道口':{
                '谷歌':{},
                '网易':{},
                'sohu':{},
                '快手':{},
            },
            '中关村':{
                'youku':{},
                'Iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{},
            },

        },
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛':{},
                '摩根':{},
            },
        },
        '闵行':{},
        '静安':{},
    },
    '山东':{
        '济南':{},
        '德州':{
            '乐陵':{
                '丁务镇':{},
                '城区':{},
            },
            '平原':{},
        },
        '青岛':{},
    }}

while True:
    for i in data:
        print('>',i)
    choice1 = input('>请选择一级菜单,或者q退出')
    if choice1 in data:
        print('进入二级菜单')
        while True:
            for i2 in data[choice1]:
                print('>>',i2)
            choice2 = input('>>请选择二级菜单,或者b返回')
            if choice2 in data[choice1]:
                print('进入三级菜单')
                while True:
                    for i3 in data[choice1][choice2]:
                        print('>>>',i3)
                    choice3 = input('>>>请选择三级菜单,或者b返回')
                    if choice3 in data[choice1][choice2]:
                        print('已经到菜单底部')
                    elif choice3 == 'b':
                        print('返回')
                        break
                    else:
                        print('输入不正确')
                        continue
            elif choice2 == 'b':
                print('返回')
                break
            else:
                print('输入不正确，重新输入')
    elif choice1 == 'q':
        break
    else:
        print('请输入菜单或者q')
