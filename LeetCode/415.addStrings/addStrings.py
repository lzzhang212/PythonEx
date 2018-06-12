#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-12 11:14:37
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 11:18:41

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()
        num2.reverse()
        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for i in range(len(num2)):
            temp = int(num1[i]) + int(num2[i]) + carry
            if temp > 9:
                carry = 1
                num1[i] = str(temp - 10)
            else:
                carry = 0
                num1[i] = str(temp)
        for i in range(len(num2), len(num1)):
            temp = int(num1[i]) + carry
            if temp > 9:
                carry = 1
                num1[i] = str(temp - 10)
            else:
                carry = 0
                num1[i] = str(temp)
                break
        if carry:
            num1.append('1')
        num1.reverse()
        return ''.join(num1)