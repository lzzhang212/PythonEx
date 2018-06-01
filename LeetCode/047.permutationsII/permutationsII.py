#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-01 09:27:24
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-01 09:41:43

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set([])
        nums.sort()
        def dfs(nums, path, res, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                visited.add(i)
                path.append(nums[i])
                dfs(nums, path, res, visited)
                path.pop()
                visited.discard(i)

        dfs(nums, [], res, visited)
        return res