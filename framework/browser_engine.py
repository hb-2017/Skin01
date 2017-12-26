#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import  configparser
import os
from selenium import webdriver
from framework.logger import Logger

#实例化Logger类
logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine():

    #获取相对路劲并且把相对路劲的最后一层目录去除
    dir = os.path.dirname(os.path.abspath('.'))
    #完善浏览器驱动的路径
    Chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    #从配置文件读取需要使用的浏览器驱动类型，并运行他
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        #配置文件的路径
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        #读取配置文件，将要启动的驱动类型
        browser = config.get('browserType','browserName')
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)
        #驱动启动，写日志
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.Chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        #打开网址并且写入日志
        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    #退出浏览器
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

