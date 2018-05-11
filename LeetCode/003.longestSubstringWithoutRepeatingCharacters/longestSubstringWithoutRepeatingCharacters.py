#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-10 19:04:31
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-10 19:05:06

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0
        for i,c in enumerate(s):
            if c in d:
                start = max(start, d[c]+1)
            d[c] = i
            ans = max(ans, i - start + 1)
        return ans