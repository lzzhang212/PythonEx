#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 17:03:06
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 17:05:26

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x^y
        ans = 0
        while n > 0:
            ans += 1
            n = n&(n - 1)       #只统计1的个数
        return ans