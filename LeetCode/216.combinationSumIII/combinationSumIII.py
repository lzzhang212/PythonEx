#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-06 09:12:37
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-06 10:39:20

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(start, path, ans, k, n):
            if k == 0 and n == 0:
                ans.append(path + [])
                return
            if k < 0 or n < 0:
                return

            for i in range(start, 10):
                path.append(i)
                dfs(i+1, path, ans, k-1, n-i)
                path.pop()

        ans = []
        dfs(1, [], ans, k, n)
        return ans