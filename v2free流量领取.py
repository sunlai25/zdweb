# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:38:06 2022

@author: sunlai
"""

from selenium import webdriver
import time
import datetime

shijian = datetime.datetime.now()
wenjian="程序提醒.txt"
try:
    #打开需要的chrome 网页
    driver = webdriver.Chrome()
    driver.set_window_size(800,800)
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
    #流量领取
    driver.find_element_by_xpath('//*[@id="checkin"]').click()  
    time.sleep(2)
    #取得系统时间并记录结果
    #open()函数参数‘w’‘r’‘r+’‘a’分别为写 读 读写 附加（不清空原内容）
    with open(wenjian,'a')as wenjian_cg:
        wenjian_cg.write("\n流量领取成功了" +shijian.strftime('%y-%m-%d %H:%M'))
    driver.quit()


except:
    print("程序发生异常，领取失败")
    with open(wenjian,'a')as wenjian_sb:
        wenjian_sb.write("\n程序发生异常，领取失败"+shijian.strftime('%y-%m-%d %H:%M'))
    time.sleep(2)
    
    driver.quit()
    