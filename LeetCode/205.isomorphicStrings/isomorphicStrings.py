#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 14:05:38
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 14:14:15

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

    def isIsomorphic2(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                if s[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
