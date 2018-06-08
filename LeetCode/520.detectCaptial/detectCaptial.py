#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 10:46:48
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 10:52:38
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        return word.istitle()