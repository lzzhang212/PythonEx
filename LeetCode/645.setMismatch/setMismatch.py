#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-11 15:06:57
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 10:46:42

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = list(set(nums))
        sums = sum([i for i in range(1, len(nums) + 1)])
        return [sum(nums)-sum(temp), sums-sum(temp)]