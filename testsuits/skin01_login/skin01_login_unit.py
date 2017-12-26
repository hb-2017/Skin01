#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from pageobjects.skin01_login_page import skin01_login_page
from get_excel.login_data import login_data
import time
from MyException.MyException import MyException



#实例化日志类
logger = Logger(logger = "skin01_login").getlog()


class skin01_login(unittest.TestCase):

    def setUp(self):
        #测试固件的setUp()的代码，主要是测试的前提准备工作
        browser = BrowserEngine(self)
        self.browser  = browser.open_browser(self)

    def tearDown(self):
        # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
        self.browser.quit()


    def skin01_login_Success(self,username,password):
        login_page = skin01_login_page(self.browser)
        login_page.input_userinfo(username,password)
        self.browser.find_element_by_id('submit').click()
        try:
            assert '易打单 | 批量打印' in login_page.get_page_title()
            print('lonin_test pass')
        except Exception as e:
            print('Test Fail.', format(e))



    def test_skin01_login(self):
        loginvalues = login_data.get_loginvalue(self)
        for loginvalue in loginvalues:
            login_page = skin01_login_page(self.browser)
            login_page.input_userinfo(loginvalue[0], loginvalue[1])
            self.browser.find_element_by_id('submit').click()
            time.sleep(3)
            try:
                if login_page.get_page_title() =='易打单 登录':
                    error_tip = login_page.get_error_tips()
                    if error_tip == '请输入图片验证码':
                        login_page.input_code()
                        logger.info('error tips input code')
                        self.browser.find_element_by_id('submit').click()
                        time.sleep(3)
                        try:
                            if login_page.get_page_title() == '易打单 | 批量打印':
                                logger.info('%s lonin_test pass' % loginvalue[0])
                                print('%s lonin_test pass' % loginvalue[0])
                                break
                        except Exception as a:
                            logger.error('%s lonin_test fail' % loginvalue[0])
                            print('Test Fail.', format(a))

                    elif error_tip==loginvalue[2]:
                        logger.info('%s lonin_test fail,error is %s' % (loginvalue[0],error_tip))
                        print('%s lonin_error_tip pass'%loginvalue[0])
                    else:
                        logger.error('%s lonin_test fail,error is %s' % (loginvalue[0],error_tip))
                        #提示信息不对则抛出异常
                        # raise MyException('error_tip: %s !=loginvalue[2]：%s'%(error_tip,loginvalue[2]))
                elif login_page.get_page_title() == '易打单 | 批量打印':
                    logger.info('%s lonin_test pass' % loginvalue[0])
                    print('%s lonin_test pass' % loginvalue[0])
                    #截图
                    login_page.get_windows_img()
                    break
            except Exception as e:
                logger.error('%s lonin_test fail' % loginvalue[0])
                print('Test Fail.', format(e))
                # raise MyException('my excepition is raised %s'%e)


#
if __name__ == '__main__':
    unittest.main()
