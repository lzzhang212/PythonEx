#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-04 11:01:04
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-07 17:10:17

import pdb

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        i = 0

        while True:
            try:
                tmp = strs[0][i]
                for item in strs:
                    if item[i] != tmp:
                        return prefix
            except:
                return prefix
            prefix += tmp
            i += 1
        return prefix

if __name__ == '__main__':
    sol = Solution()
    str1 = ["flower","flow","flight"]
    #pdb.set_trace()
    print(sol.longestCommonPrefix(str1))




