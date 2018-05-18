#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-17 15:38:52
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-17 15:42:59

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            ans += 1
            n = (n-1)&n
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(1))
    print(sol.hammingWeight(2))
    print(sol.hammingWeight(1023))