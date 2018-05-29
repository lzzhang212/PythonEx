#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-29 08:54:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-29 08:56:25

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        r_set = set(ransomNote)
        for ch in r_set:
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True