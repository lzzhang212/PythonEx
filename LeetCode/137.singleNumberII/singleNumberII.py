#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 14:04:40
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 14:17:24

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counterOne = counterTwo = 0
        for i in range(len(nums)):
            counterOne = (~counterTwo)&(counterOne^nums[i])
            counterTwo = (~counterOne)&(counterTwo^nums[i])
        return counterOne

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def singleNumberK(nums, k):
            count = [0]*32
            ret = 0
            for i in range(32):
                for each in nums:
                    if each & (1 << i):
                        count[i] += 1
                if count[i] % k:
                    ret |= (1 << i)
            if ret > 0x7fffffff:
                ret -= 0x100000000
            return ret
        return singleNumberK(nums, 3)
