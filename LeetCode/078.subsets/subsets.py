#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-30 11:14:00
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-30 11:14:44

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in nums:
            ans = ans + [[i] + num for num in ans]
        return ans