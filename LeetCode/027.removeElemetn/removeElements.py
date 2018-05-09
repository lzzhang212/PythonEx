#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 08:49:54
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 09:17:20

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for i in reversed(range(0,len(nums))):
            if nums[i] == val:
                del nums[i]
        
        return len(nums)