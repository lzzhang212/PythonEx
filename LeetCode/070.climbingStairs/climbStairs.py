#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 10:23:51
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 13:43:53

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #cs(n) = cs(n-1) + cs(n-2)
        if n <= 1:
            return 1
        cs[0],cs[1],cs[2] = 1,1,2
        for i in range(3,n+1):
            cs[i] = cs[i-1] + cs[i-2]
        return cs[n]