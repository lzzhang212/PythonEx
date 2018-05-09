#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 15:06:30
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 17:12:04

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
        i = 0
        j = 0
        next_list = self.getNext(needle)
        while i < h_len and j < n_len:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_list[j]
        if j == n_len:
            return i - j     
        return -1
    
    def getNext(self, pattern):
        i = 0
        j = -1
        next_list = []
        for x in range(0,len(pattern)):
            next_list.append(-1)
        print(next_list)
        while i < len(pattern):
            if j == -1 or pattern[i] == pattern[j]:
                i += 1
                j += 1
                print(i,j)
                next_list[i] = j
            else:
                j = next_list[j]
        return next_list

if __name__ == '__main__':
    sol = Solution()
    haystack = 'hello'
    needle = 'll'
    print(sol.strStr(haystack, needle))