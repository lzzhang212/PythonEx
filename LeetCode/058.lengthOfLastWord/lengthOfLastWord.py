#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 09:19:48
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 09:19:55

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s1 = s.strip().split()
        if len(s1) == 0:
            return 0
        else:
            return len(s1[-1])