#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-14 19:45:00
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-14 19:50:16

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        negFlag = False
        if num < 0:
            negFlag = True
            num = abs(num)
        tmp = []
        while num:
            tmp.append(str(num%7))
            num //= 7
        tmp.reverse()
        res = ''.join()
        if negFlag:
            res = '-' + res
        return res