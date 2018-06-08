#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 11:15:15
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 11:17:39

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def findNextGreater(nums, index, value):
            for i in range(index, len(nums)):
                if nums[i] > value:
                    return nums[i]
            return -1

        d = {}
        ans = []
        for i,j in enumerate(nums2):
            d[j] = i
        for i in range(len(nums1)):
            ans.append(findNextGreater(nums2, d[nums1[i]], nums1[i]))
        return ans