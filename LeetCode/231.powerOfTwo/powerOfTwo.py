#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 18:34:01
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 18:35:24

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n-1)&n == 0