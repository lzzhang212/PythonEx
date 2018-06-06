#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-06 10:45:31
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-06 10:45:40

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        i = 0
        while i < (1<<n):
            ans.append(i^(i>>1))
            i += 1
        return ans