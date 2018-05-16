#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 16:10:09
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 16:13:14

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end],s[start]
                start += 1
                end -= 1

        k %= len(nums)
        start = 0
        end = len(nums) - 1
        reverse(start, k-1, nums)
        reverse(k, end, nums)
        reverse(start, end, nums)