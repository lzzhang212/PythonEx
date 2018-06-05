#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-05 09:57:38
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-05 10:01:58

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -nums[idx]
            if nums[idx] > 0:
                ans.append(idx + 1)
        return ans