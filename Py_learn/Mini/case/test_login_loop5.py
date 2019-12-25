# -*- coding:utf-8 -*-
# Author:Jin Fei
import unittest
from appium import webdriver
import time,os
from Mini.Function.common import *


def isElementExist(element):
        #判断元素
        flag=True
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag
i = 0
while i < 5:
            desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '9',
                    'deviceName': 'a57c5aae',
                    'appPackage': 'com.tencent.mm',
                    'appActivity': 'com.tencent.mm.ui.LauncherUI',
                    'automationName': 'Uiautomator2',
                    # 'udid': 'a57c5aae',
                    # 'resetKeyboard': True,
                    'noReset': True,
                    "automationName": "uiautomator2"
                    }
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
            driver.implicitly_wait(8)

            """登录并进入家电列表页面"""
            time.sleep(3)
            window = driver.get_window_size()
            x1 = window['width'] * 0.5  # 起始x坐标
            y1 = window['height'] * 0.2  # y1坐标，滑动起始点
            y2 = window['height'] * 0.7  # y2坐标，滑动末尾点
            driver.swipe(x1,y1,x1,y2,500) # 页面下拉
            time.sleep(2)
            driver.find_element_by_id('com.tencent.mm:id/ka').click() # 点击进入小程序
            time.sleep(2)
            add_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[3]/android.view.View[3]"
            driver.find_element_by_xpath(add_xpath).click()
            time.sleep(2)
            login1_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View"
            driver.find_element_by_xpath(login1_xpath).click()
            time.sleep(2)
            inputbox_account_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View"
            driver.find_element_by_xpath(inputbox_account_xpath).click()
            time.sleep(2)
            #点开数字键盘
            driver.tap([(230, 2023),(230, 2023)],100)
            time.sleep(2)
            driver.tap([(293, 1544)],100)#1([(293, 1544),(293, 1544)],100)
            time.sleep(1)
            driver.tap([(777, 1554)],100)#3([(777, 1554),(777, 1554)],100)
            time.sleep(1)
            driver.tap([(533, 1539)],100)#2([(533, 1539),(533, 1539)],100)
            time.sleep(1)
            driver.tap([(288, 1862)],100)#7([(288, 1862),(288, 1862)],100)
            time.sleep(1)
            driver.tap([(547, 2009)],100)#0([(547, 2009),(547, 2009)],100)
            time.sleep(1)
            driver.tap([(533, 1862)],100)#8([(533, 1862),(533, 1862)],100)
            time.sleep(1)
            driver.tap([(288, 1862)],100)#7([(288, 1862),(288, 1862)],100)
            time.sleep(1)
            driver.tap([(782, 1706)],100)#6([(782, 1706),(782, 1706)],100)
            time.sleep(1)
            driver.tap([(777, 1554)],100)#3([(777, 1554),(777, 1554)],100)
            time.sleep(1)
            driver.tap([(547, 2009)],100)#0([(547, 2009),(547, 2009)],100)
            time.sleep(1)
            driver.tap([(787, 1872)],100)#9([(787, 1872),(787, 1872)],100)
            time.sleep(2)
            #inputbox_pwd_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View"
            #time.sleep(2)
            #self.driver.find_element_by_xpath(inputbox_pwd_xpath).click()
            #self.driver.tap([(100, 400)],100)#点击屏幕空白位置
            #time.sleep(5)
            inputbox_pwd_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View"
            time.sleep(2)
            try:
                driver.find_element_by_xpath(inputbox_pwd_xpath).click()
            except:
                print("没有点击进入密码输入，请求再次点击")
                driver.find_element_by_xpath(inputbox_pwd_xpath).click()
            time.sleep(2)
            time.sleep(2)
            driver.tap([(59, 1544)],100)#q
            time.sleep(1)
            driver.tap([(166, 1554)],100)#w
            time.sleep(1)
            driver.tap([(274, 1544)],100)#e
            time.sleep(1)
            driver.tap([(376, 1549)],100)#r
            time.sleep(1)
            driver.tap([(220, 2023)],100)
            time.sleep(1)
            driver.tap([(288, 1549)],100)#1
            time.sleep(1)
            driver.tap([(542, 1549)],100)#2
            time.sleep(1)
            driver.tap([(777, 1554)],100)#3
            time.sleep(1)
            driver.tap([(303, 1706)],100)#4
            time.sleep(1)
            driver.tap([(88, 1539)],100)#.
            time.sleep(1)
            driver.tap([(547, 1139)],100)
            time.sleep(1)
            driver.tap([(518, 1569)],100)
            time.sleep(3)
            #注销
            time.sleep(8)
            driver.tap([(933, 2023)],100)
            time.sleep(5)
            logout_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[3]/android.view.View/android.view.View[4]/android.view.View"
            exist1 = isElementExist(logout_xpath)
            if exist1:
                print("找到注销控件")
            else:
                print("没有找到注销控件")
            driver.find_element_by_xpath(logout_xpath).click()
            driver.quit()
            print(i)
            i += 1