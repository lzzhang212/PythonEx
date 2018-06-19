#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-15 11:37:59
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-15 11:38:09

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        diffCandies = set(candies)
        return min(len(diffCandies), len(candies)//2)