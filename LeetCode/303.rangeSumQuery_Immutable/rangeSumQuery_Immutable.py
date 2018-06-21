#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-21 17:53:02
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-21 17:54:56

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.leftSum = []
        res = 0
        for i in range(len(nums)):
            res += nums[i]
            self.leftSum.append(res)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.leftSum[j]
        else:
            return self.leftSum[j] - self.leftSum[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)