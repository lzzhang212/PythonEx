#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 09:43:26
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 09:55:34

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxRob = before = 0
        for i in range(0, len(nums)):
            tmp = maxRob
            maxRob = max(before + nums[i], maxRob)
            before = tmp
        return maxRob