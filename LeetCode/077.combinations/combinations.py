#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-30 11:30:31
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-30 11:34:27

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        elif k == n:
            return [[i for i in range(1, n+1)]]
        else:
            ans = []
            ans += self.combine(n-1, k)
            part = self.combine(n-1, k-1)
            for ls in part:
                ls.append(n)
            ans += part
            return ans