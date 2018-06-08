#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 11:28:00
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 11:28:45

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num
        valid = 0
        while tmp:
            tmp //= 2
            valid += 1
        return ~num & ((1<<valid) - 1)