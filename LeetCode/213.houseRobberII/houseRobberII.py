#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 09:56:55
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 10:08:19

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def maxRob(start, end, nums):
            maxMoney = before = 0
            for i in range(len(nums)):
                tmp = maxMoney
                maxMoney = max(before + nums[i], maxMoney)
                before = tmp
            return maxMoney
        return max(maxRob(0, len(nums)-1, nums), maxRob(0, len(nums), nums))
