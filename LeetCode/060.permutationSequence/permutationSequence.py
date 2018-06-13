#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 14:41:43
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 14:45:14

import math
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 穷举解法超时
        # def dfs(path, res, nums, visited):
        #     if len(path) == len(nums):
        #         res.append(path + [])
        #         return
            
        #     for i in range(len(nums)):
        #         if i not in visited:
        #             path.append(nums[i])
        #             visited.append(i)
        #             dfs(path, res, nums, visited)
        #             visited.pop()
        #             path.pop()
        # ans = []
        # visited = []
        # nums = [i for i in range(1,n+1)]
        # dfs([], ans, nums, visited)
        # return ''.join('%s' %each for each in ans[k-1])
        
        fact = [math.factorial(n-i-1) for i in range(n)]
        visited = [0 for _ in range(n)]
        ans = ''
        k -= 1
        for i in range(n):
            t = k//fact[i]
            for j in range(n):
                if not visited[j]:
                    if t == 0:
                        break
                    t -= 1
            ans += str(j+1)
            k %= fact[i]
            visited[j] = 1
        return ans