#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 08:49:18
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 08:49:32

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        key = nums[-1]
        for i in reversed(range(0,len(nums)-1)):
            if nums[i] == key:
                del(nums[i])
            else:
                key = nums[i]
        
        return len(nums)