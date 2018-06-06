#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-06 10:40:58
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-06 10:44:18

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = index = -1
        for i,j in enumerate(nums):
            if j > maxnum:
                index, maxnum = i, j

        for i,j in enumerate(nums):
            if i = index:
                continue
            if 2*j > maxnum:
                return -1
        return index

