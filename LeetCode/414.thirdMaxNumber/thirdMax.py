#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 08:55:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 08:55:58

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        nInf = float('-Inf')
        max3 = [nInf, nInf, nInf]
        for i in range(len(nums)):
            if nums[i] not in max3:
                if nums[i] > max3[0]:
                    max3[2] = max3[1]
                    max3[1] = max3[0]
                    max3[0] = nums[i]
                elif nums[i] > max3[1]:
                    max3[2] = max3[1]
                    max3[1] = nums[i]
                elif nums[i] > max3[2]:
                    max3[2] = nums[i]
        return max3[2] if max3[2] != nInf else max3[0]