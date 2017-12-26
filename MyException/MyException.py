#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

class MyException(Exception):

    def __init__(self,message):
        print()
        Exception.__init__(self)
        self.message=message