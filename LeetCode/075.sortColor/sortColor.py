#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 16:20:16
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 16:50:18

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        for i in range(j, len(nums)):
            if nums[i] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1