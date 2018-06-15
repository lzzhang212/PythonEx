#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-14 20:10:18
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-15 10:10:24

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        start = 0
        for each in nums:
            if each == 1:
                temp += 1
                maxLen = max(maxLen, temp)
            else:
                temp = 0
        return maxLen