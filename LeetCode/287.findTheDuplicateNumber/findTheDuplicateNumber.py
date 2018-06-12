#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-11 14:48:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-11 15:05:55

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = len(nums) - 1    #right = n
        mid = (left + right) >> 1
        while left < right:
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) >> 1
        return left