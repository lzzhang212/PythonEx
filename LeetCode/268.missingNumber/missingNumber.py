#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 18:25:37
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 18:31:03

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        return (n*n+1)/2 - sum(nums)

    def missingNumber2(self, nums):
        if not nums:
            return None
        res = len(nums)
        for i in range(res):
            ans += (i - nums[i])