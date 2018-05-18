#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-17 19:25:02
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-17 19:30:58

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        exist = [True for _ in range(n)]
        count = n - 2
        p = 2
        while p*p <= n:
            if exist[p]:
                j = p*p
                while j < n:
                    if exist[j]:
                        exist[j] = False
                        count -= 1
                    j += p
            p += 1
        print(exist)
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(1000))