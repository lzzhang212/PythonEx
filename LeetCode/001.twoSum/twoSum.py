#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-03 11:11:38
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-03 14:16:47

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums,target))