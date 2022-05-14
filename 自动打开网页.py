# -*- coding: utf-8 -*-
"""
Created on Sat May 14 09:51:21 2022

@author: sunlai
"""
from selenium import webdriver
import time
import pyautogui


#打开需要的chrome 网页
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://w1.v2dns.xyz/user')

#调用selenium 库中的find_element_by_xpath()方法定位搜索框
#同时使用send_keys()方法在其中输入信息
time.sleep(5)
driver.find_element_by_xpath('//*[@id="email"]').send_keys("153732378@qq.com")
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("Sun251989")

#调用selenium库中的find_element_by_xpath()方法定位搜索框
#用click（）方法对按钮点击
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(10)

#调用图形识别
#鼠标移动 滑轮滚下
img_path1 = r'D:\迅雷下载\2.png'
pos = pyautogui.locateOnScreen(img_path1)
zhong=pyautogui.center(pos)
pyautogui.moveTo(zhong, duration=1)
pyautogui.scroll(-1000)
time.sleep(1)

#找到图片位置 并将鼠标移至此处
img_path2 = r'D:\迅雷下载\1.png'
pos1 = pyautogui.locateOnScreen(img_path2)
zhong1=pyautogui.center(pos1)

#双击鼠标左键领取流量
pyautogui.moveTo(zhong1, duration=1)
pyautogui.doubleClick(zhong1)
time.sleep(5)

driver.quit()
