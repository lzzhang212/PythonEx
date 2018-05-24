#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 08:39:08
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 08:54:54

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        if len(s) == 1:
            return 0
        letters = [0]*26
        #统计s中每个字母出现的次数
        for ch in s:
            ci = ord(ch) - ord('a')
            letters[ci] += 1

        #根据letters找到s中第一个出现次数为1的字母
        for i in range(len(s)):
            ci = ord(s[i]) - ord('a')
            if letters[ci] == 1:
                return i
        return -1