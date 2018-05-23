#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 19:56:56
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 19:57:00

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 != 0:
                res.append('Fizz')
            elif i%3 != 0 and i%5 == 0:
                res.append('Buzz')
            elif i%3 == 0 and i%5 == 0:
                res.append('FizzBuzz')
            else:
                res.append(str(i))
        return res