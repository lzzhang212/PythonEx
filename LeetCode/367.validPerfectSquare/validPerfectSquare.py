#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-29 09:00:54
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-29 09:03:27

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left < right:
            mid = (left + right)//2
            if mid**2 > num:
                right = mid
            else:
                left = mid + 1
        if left > 1:
            sqrt_num = left - 1
        else:
            sqrt_num = left
        return sqrt_num**2 == num