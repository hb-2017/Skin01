#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from framework.base_page import Basepage

class skin01_login_page(Basepage):

    # 账户名,密码，记住密码，登录
    username = 'id=>userName'
    password = 'id=>passWord'
    remember_password = 'id=>remeber'
    sumbit = 'id=>submit'

    # 错误信息，验证码图片，验证码输入
    error_tips = 'id=>error_tips'
    captchaImg = 'id=>captchaImg'
    captcha = 'id=>captcha'

    #第三方登录按钮
    taobaoLogin = 'id=>taobaoLogin'
    qqLogin = 'id=>qqLogin'
    weixinLogin = 'id=>weixinLogin'

    #注册,忘记密码
    free_reg = 'id=>free_reg'
    forget_pwd = 'id=>forget_pwd'



    #输入账号密码
    def input_userinfo(self,username,password):
        self.input(self.username,username)
        self.input(self.password,password)

    #点击登录
    def click_login(self):
        self.click(self.sumbit)
        self.sleep(2)

    #获取错误信息并返回
    def get_error_tips(self):
        element = self.find_element(self.error_tips)
        element_text = element.text
        return element_text

    # 输入验证码
    def input_code(self):
        code = input('请输入登录图片验证码')
        self.input(self.captcha,code)




