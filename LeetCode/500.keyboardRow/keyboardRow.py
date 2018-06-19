#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-15 11:20:39
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-15 11:27:26

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiopQWERTYUIOP'
        row2 = 'asdfghjklASDFGHJKL'
        row3 = 'zxcvbnmZXCVBNM'
        ans = lsit(filter(lambda x: set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3), words))
        return ans