#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from selenium import webdriver
import time

url = 'https://www.1dadan.com'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_id('taobaoLogin').click()
time.sleep(2)
aa = browser.find_element_by_class_name('openplatform-login-header-content').text
print(aa)
browser.switch_to.frame("J_loginIframe")
div=browser.find_element_by_id('J_LoginBox')
div.find_element_by_id('TPL_username_1').send_keys('卖xxxx的小魔王')
browser.find_element_by_id('TPL_password_1').send_keys('huya19960904')