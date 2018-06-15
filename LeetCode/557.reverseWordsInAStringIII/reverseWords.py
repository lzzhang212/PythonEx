#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-15 10:22:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-15 10:23:27

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split(' ')
        res = []
        for each in word:
            res.append(each[::-1])
        return ' '.join(res)