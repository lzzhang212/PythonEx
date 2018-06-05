#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-05 09:26:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-05 09:56:11

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans