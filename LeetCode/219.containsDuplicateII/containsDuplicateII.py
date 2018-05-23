#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 17:06:20
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 17:06:22

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        if k == 0:
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False