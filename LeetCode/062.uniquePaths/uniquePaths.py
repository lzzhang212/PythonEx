#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-07 09:31:34
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-07 09:33:20

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[-1]