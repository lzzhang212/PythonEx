#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 15:06:30
# @Last Modified by:   zhlz_home
# @Last Modified time: 2018-05-09 23:49:32

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        i = j = 0
        while i < h_len and j < n_len:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j = 0
        if j == n_len:
            return i-j
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    haystack = 'hello'
    needle = 'll'
    print(sol.strStr(haystack, needle))