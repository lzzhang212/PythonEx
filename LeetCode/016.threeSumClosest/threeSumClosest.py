#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-15 15:42:09
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-15 15:42:15

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('Inf')
        ans = 0
        for i in range(0,len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                if diff > abs(sums - target):
                        diff = abs(sums - target)
                        ans = sums
                if sums > target:
                    end -= 1
                else:
                    start += 1
        
        return ans