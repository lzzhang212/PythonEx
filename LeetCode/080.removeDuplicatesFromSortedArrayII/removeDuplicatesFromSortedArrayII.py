#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 14:57:20
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 15:05:13

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i = j = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count <= 2:
                    nums[j] = nums[i]
                    j += 1
            else:
                nums[j] = nums[i]
                j += 1
                count = 1
        return j