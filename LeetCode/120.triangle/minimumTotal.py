#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 09:00:17
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 09:00:20

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        if depth == 0:
            return 0
        dp = triangle[-1]
        for i in reversed(range(depth-1)):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]