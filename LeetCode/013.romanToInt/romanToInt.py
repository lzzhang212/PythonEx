#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-04 09:58:32
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-04 10:46:40

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0

        for i in range(len(s)-1):
            c = s[i]
            cafter = s[i+1]
            if d[c] < d[cafter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans += d[s[-1]]
        return ans

if __name__ == '__main__':
    sol = Solution()
    s1 = 'III'
    s2 = 'IV'
    s3 = 'IX'
    s4 = 'LVIII'
    s5 = 'MCMXCIV'
    print(s1+' : ',sol.romanToInt(s1))
    print(s2+' : ',sol.romanToInt(s2))
    print(s3+' : ',sol.romanToInt(s3))
    print(s4+' : ',sol.romanToInt(s4))
    print(s5+' : ',sol.romanToInt(s5))