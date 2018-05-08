#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-03 15:01:00
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-03 19:34:29

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(abs(x))
        order = []
        for i in str_x:
            order.append(i)
        order.reverse()
        str_x = ''.join(order)
        if x < 0:
            y = -1*int(str_x)
        else:
            y = int(str_x)

        if y > 2**31 - 1 or y < -2**31:
            return 0
        else:
            return y

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123456789))
    print(s.reverse(-123456789876543219))
    print(s.reverse(333281565989))
    print(s.reverse(1563847412))