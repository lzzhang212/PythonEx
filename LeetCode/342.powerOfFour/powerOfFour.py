#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 15:31:01
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 15:32:10

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        #筛掉非2的幂的数
        if num & (num-1) != 0:
            return False
        #4的幂二进制的1都在奇数位上
        return (num & 0x55555555) != 0