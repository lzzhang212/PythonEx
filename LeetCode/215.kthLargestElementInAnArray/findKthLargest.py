#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-19 14:36:29
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-19 14:37:04

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums.[-k]