#!/usr/bin/env python
# encoding: utf-8

"""
@author: z00390414
@software: PyCharm
@file: test3.py
@time: 2017/8/17 19:38
"""

# coding:utf-8
from django.test import TestCase

class MyTest(TestCase):
    def setUp(self):
        number=input("Enter a number:")   #input输入信息
        self.number=int(number)

    def test_case(self):
        self.assertEqual(self.number,10,msg="Your input is not 10")