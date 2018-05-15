#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-03 19:44:11
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-03 19:57:56

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0 or x < 10:
            return True

        l1 = []
        l2 = []
        while x > 0:
            l1.append(x%10)
            l2.append(x%10)
            x = x//10

        l1.reverse()
        if l1 == l2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(0))
    print(s.isPalindrome(9))

