#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-15 10:06:10
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-15 10:10:16

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums, reverse = True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]
        num2rank = dict(zip(sort, rank))
        return [num2rank[num] for num in nums]