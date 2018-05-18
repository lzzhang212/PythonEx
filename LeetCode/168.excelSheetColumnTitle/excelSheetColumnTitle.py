#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-18 16:37:16
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-18 16:44:14

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n > 0:
            y = n % 26
            if y == 0:
                char = 'Z'
            else:
                char = chr(ord('A') + y -1)
            ans += char
            n //= 26
        return ans[::-1]
