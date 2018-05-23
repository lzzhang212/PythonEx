#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 18:14:48
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 18:24:31

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return (num - 1)%9 + 1

    def addDigits2(self, num):
        ans = num
        while True:
            if res < 10:
                return res
            num = res
            res = 0
            while num:
                res += num%10
                num //= 10