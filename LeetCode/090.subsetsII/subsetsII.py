#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-01 17:16:47
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-01 17:17:00

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, nums, path, res, visited):
            res.append(path + [])
            
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(i + 1, nums, path, res, visited)
                    path.pop()
                    visited.discard(i)
        nums.sort()
        visited = set([])
        res = []
        dfs(0, nums, [], res, visited)
        return res