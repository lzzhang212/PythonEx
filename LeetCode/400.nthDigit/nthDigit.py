#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-12 18:14:14
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 18:19:11

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, step = 1, 1, 9
        while n > size*step:
            n -= step*size
            size += 1
            start *= 10
            step *= 10
        return int(str(start + (n-1)//size)[(n-1)%size])