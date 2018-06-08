#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 15:07:27
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 15:09:18

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for p1 in points:
            d = {}
            for p2 in points:
                if p1 != p2:
                    dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                    d[dist] = d.get(dist, 0) + 1
            for k in d:
                ans += d[k]*(d[k] - 1)
        return ans