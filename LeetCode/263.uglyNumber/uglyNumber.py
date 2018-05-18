#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-17 19:40:43
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-17 19:43:23

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num%2 == 0 or num%3 == 0 or num%5 == 0:
            if num%2 == 0:
                num /= 2
            if num%3 == 0:
                num /= 3
            if num%5 == 0:
                num /= 5
        return num == 1