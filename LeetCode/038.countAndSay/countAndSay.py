#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-07 16:04:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-07 16:22:50

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        index = 1
        while index < n:
            preCh = string[0]
            nextStr = ''
            count = 0
            for ch in string:
                if ch == preCh:
                    count += 1
                else:
                    nextStr += str(count) + preCh
                    preCh = ch
                    count = 1
            nextStr += str(count) + preCh
            string = nextStr
            index += 1
        return string 