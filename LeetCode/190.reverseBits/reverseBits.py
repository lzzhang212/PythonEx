#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 09:29:53
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 09:31:10

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            if n & mask:
                ans |= 1
            n >>= 1
        return ans