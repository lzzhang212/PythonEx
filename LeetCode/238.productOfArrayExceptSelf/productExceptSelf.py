#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-19 14:40:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-19 17:13:45

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in range(len(nums))]
        right = 1
        for i in range(1, len(nums)):
            res[i] *= res[i-1]*nums[i-1]
        for i in reversed(range(len(nums) - 1)):
            right *= right*nums[i+1]
            res[i] *= right
        return res