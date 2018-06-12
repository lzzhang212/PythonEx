#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-12 11:38:17
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 13:31:43

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    g = [1,2,3]
    s = [1,1]
    print(sol.findContentChildren(g,s))