#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-17 20:02:10
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-17 20:06:45

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        got = set()
        while n != 1 and n not in got:
            got.add(n)
            temp_sum = 0
            while n > 0:
                temp_sum += (n%10)**2
                n //= 10
            n = temp_sum
        return n == 1