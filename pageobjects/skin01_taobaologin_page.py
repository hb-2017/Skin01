#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from framework.base_page import Basepage
from framework.browser_engine import BrowserEngine


class skin01_taobaologin_page(Basepage):

    #切换登录
    J_Static2Quick = 'id=>J_Static2Quick' #快速登录
    J_Quick2Static = 'id=>J_Quick2Static' #账号密码登录

    #授权登录
    J_SubmitStatic = 'id=>J_SubmitStatic'

    #账号是否登录
    taobaologin_statu_ = 'x=>/html/body/div/div[2]/div[1]/h3'

    # 账号，密码
    TPL_username_1 = 'id=>TPL_username_1'
    TPL_password_1 = 'id=>TPL_password_1'


    # 输入账号密码
    def input_taobaoinfo(self,username,password):
        self.browser.switch_to.frame("J_loginIframe")
        self.clear(self.TPL_username_1)
        self.clear(self.TPL_password_1)
        self.input(self.TPL_username_1,username)
        self.input(self.TPL_password_1,password)


    #判断是否登录了淘宝
    def taobaologin_statu(self):
        tb_statu = self.element_is_dispalynd(self.taobaologin_statu_)
        return tb_statu




