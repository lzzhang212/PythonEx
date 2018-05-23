#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 18:32:19
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 18:32:59

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        while True:
            num = (start + end)//2
            if guess(num) == 0:
                return num
            elif guess(num) == 1:
                start = num + 1
            else:
                end = num - 1