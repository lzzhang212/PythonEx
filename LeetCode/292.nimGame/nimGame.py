#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-23 08:47:57
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-23 08:48:06

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0