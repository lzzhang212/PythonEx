#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 16:46:02
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 16:46:25

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,\
             'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,\
             'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        length = len(s)
        if not length:
            return 0
        res = 0
        for i in range(length):
            index = s[i].upper()
            base = 26**(length - 1 - i)
            res += d[index]*base
        return res