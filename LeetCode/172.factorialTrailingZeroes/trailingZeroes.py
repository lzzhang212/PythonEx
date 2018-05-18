#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 16:48:26
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 17:02:06

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            k = n // 5
            res += k
            n = k
        return res