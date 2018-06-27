#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-27 16:23:20
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-27 16:23:44

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]