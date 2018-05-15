#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-15 20:20:08
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-15 20:20:12

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return M[(num//1000)%10]+C[(num//100)%10]+X[(num//10)%10]+I[num%10]