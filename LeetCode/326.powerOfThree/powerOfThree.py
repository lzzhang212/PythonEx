#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 15:16:18
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 15:16:23

import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        maxPower = 3**(int(math.log(0x7fffffff)/math.log(3)))
        return maxPower%n == 0