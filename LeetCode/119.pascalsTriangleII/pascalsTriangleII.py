#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18/5/11 下午11:56
# @Author  : lzzhang
# @Site    : 
# @File    : pascalsTriangleII.py
# @Software: PyCharm

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def triangles():
            N = [1]
            while True:
                yield N
                N.append(0)
                N = [N[i-1]+N[i] for i in range(0,len(N))]

        for t in triangles():
            rowIndex -= 1
            if rowIndex < 0:
                break
        return t
