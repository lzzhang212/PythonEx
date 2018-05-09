#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 13:45:09
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 13:54:51

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float('-Inf')
        sum = 0
        for i in range(0,len(nums)):
            sum = max(sum + nums[i],nums[i])
            result = max(result,sum)
        return result