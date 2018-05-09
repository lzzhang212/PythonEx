#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 22:55:17
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 22:58:42

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
        next_list = self.getNext(needle)
        
        while i < h_len and j < n_len:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_list[j]
            
        if j == n_len:
            return i-j
        else:
            return -1
    
    def getNext(self,pattern):
        p_len = len(pattern)
        k = -1
        j = 0
        next_list = [-1 for i in range(0,p_len)]
        while j < p_len - 1:
            if k == -1 or pattern[k] == pattern[j]:
                k += 1
                j += 1
                if pattern[k] != pattern[j]:
                    next_list[j] = k
                else:
                    next_list[j] = next_list[k]
            else:
                k = next_list[k]
        return next_list

if __name__ == '__main__':
    sol = Solution()
    haystack = 'hello'
    needle = 'll'
    print(sol.strStr(haystack,needle))