#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-06 15:22:42
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-06 15:27:37

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    sums = nums[i] + nums[j] + nums[start] + nums[end]
                    if sums > target:
                        end -= 1
                    elif sums < target:
                        start += 1
                    else:
                        ans.append((nums[i],nums[j],nums[start],nums[end]))
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == numd[end+1]:
                            end -= 1
        return ans