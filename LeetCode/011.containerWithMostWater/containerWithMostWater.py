#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 16:05:11
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 16:28:00

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right-left)*min(height[left],height[right])):
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans
        
