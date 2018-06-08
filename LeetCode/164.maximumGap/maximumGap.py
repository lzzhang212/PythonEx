#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 17:14:54
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 17:15:06

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        maxGap = 0
        for i in range(1,len(nums)):
            maxGap = max(maxGap, abs(nums[i]-nums[i-1]))
        return maxGap