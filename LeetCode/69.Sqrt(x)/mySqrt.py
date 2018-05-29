#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-29 10:10:42
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-29 10:10:48

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = (left + right)//2
            if mid**2 > x:
                right = mid
            else:
                left = mid + 1
        if left > 1:
            sqrt_num = left - 1
        else:
            sqrt_num = left
        return sqrt_num