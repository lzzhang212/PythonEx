#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 08:29:08
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 08:42:13

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [0 for _ in range(n)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0:
                    if j == 0:
                        dp[j] = grid[i][j]
                    else:
                        dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]