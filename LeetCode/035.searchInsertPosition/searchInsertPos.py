#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 09:18:24
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 09:18:32

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            for i in range(0,len(nums)):
                if target < nums[i]:
                    return i
            return len(nums)