#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-27 16:26:39
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-27 16:26:53

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]