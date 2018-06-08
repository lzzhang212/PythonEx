#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-07 18:23:19
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-07 19:35:35

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i],[j]

        i, j = 0, n-1
        while i < j:
            for k in range(n):
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]