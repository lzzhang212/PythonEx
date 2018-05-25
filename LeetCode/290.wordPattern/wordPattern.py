#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-25 13:36:56
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-25 13:36:59

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l_str = str.split(' ')
        d = {}
        if len(pattern) != len(l_str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if l_str[i] not in d.values():
                    d[pattern[i]] = l_str[i]
                else:
                    return False
            else:
                if d[pattern[i]] != l_str[i]:
                    return False
                
        return True