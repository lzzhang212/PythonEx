#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-31 09:03:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-31 09:04:54

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in range(len(t)):
            if t.count(t[i]) != s.count(t[i]):
                return t[i]