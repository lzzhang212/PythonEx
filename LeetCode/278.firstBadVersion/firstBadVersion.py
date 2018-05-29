#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-29 08:41:45
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-29 08:44:15

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left