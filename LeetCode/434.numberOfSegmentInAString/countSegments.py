#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-29 08:45:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-29 08:45:46

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())