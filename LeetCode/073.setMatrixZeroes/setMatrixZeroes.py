#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-12 19:45:24
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 09:32:42

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        # zero = []
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             zero.append([i,j])
        # for each in zero:
        #     row = each[0]
        #     col = each[1]
        #     for i in range(m):
        #         matrix[i][col] = 0
        #     for j in range(n):
        #         matrix[row][j] = 0
        
        # O(1)空间复杂度解法:利用原矩阵第一行和第一列来标记对应列/行是否置0
        
        m = len(matrix)
        n = len(matrix[0])
        row_flag, col_flag = 0, 0
        for i in range(n):
            if matrix[0][i] == 0:
                row_flag = 1
        for i in range(m):
            if matrix[i][0] == 0:
                col_flag = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        if row_flag:
            for i in range(n):
                matrix[0][i] = 0
        if col_flag:
            for i in range(m):
                matrix[i][0] = 0
