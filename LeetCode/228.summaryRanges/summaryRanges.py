#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-19 14:39:23
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-19 14:39:25

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if start != nums[i-1]:
                    ans.append(str(start)+'->'+str(nums[i-1]))
                else:
                    ans.append(str(start))
                start = nums[i]
        if start != nums[-1]:
            ans.append(str(start)+'->'+str(nums[-1]))
        else:
            ans.append(str(start))
        return ans