#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 17:07:50
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 17:09:52

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[(len(nums)-1)//2]