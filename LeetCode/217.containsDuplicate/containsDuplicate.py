#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 16:56:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 17:00:16

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) == len(nums)

    def containsDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False