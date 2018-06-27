#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-27 16:36:32
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-27 16:36:39

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low