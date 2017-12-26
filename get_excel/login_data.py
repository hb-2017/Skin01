#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import xlrd

# 获取登录需要的账号密码
class login_data():

    def get_loginvalue(self):
        loginvalues = []
        loginvalue = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\Skin01\get_excel\Excel_info\loginvalue.xls')
        table = loginvalue.sheet_by_name(u'Sheet1')  # 通过名称获取
        nrows = table.nrows  # 获取行数
        if nrows > 1:
            for i in range(nrows - 1):
                x = table.row_values(i + 1)
                loginvalues.append(x)
            return loginvalues
        else:
            return None
            # loginvalues[username] = password


# a = login_data().get_loginvalue()
# print(a)