#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-07 19:46:57
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-07 19:51:52

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0]*n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        k = 1
        while left <= right and up <= down:
            for i in range(left, right + 1):
                ans[up][i] = k
                k += 1
            up += 1
            for i in range(up, down + 1):
                ans[i][right] = k
                k += 1
            right -= 1
            for i in reversed(range(left, right + 1)):
                ans[down][i] = k
                k += 1
            down -= 1
            for i in reversed(range(up, down + 1)):
                ans[left][i] = k
                k += 1
            left += 1
        return ans