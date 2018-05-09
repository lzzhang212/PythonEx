#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 09:45:58
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 09:46:03

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        for i in range(0,len(digits)-1):
            if digits[i] > 9:
                digits[i] = 0
                digits[i+1] += 1
        
        if digits[-1] > 9:
            digits[-1] = 0
            digits.append(1)
        digits.reverse()
        return digits