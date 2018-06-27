#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-27 16:24:47
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-27 16:25:08

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        while low < high:
            mid = (low + high)//2
            if A[mid] > A[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low