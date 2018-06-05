#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-04 10:42:53
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-04 13:21:34

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            print("NONE!")
            return []
        ans = []
        up, left, right, down = 0, 0, len(matrix[0])-1, len(matrix)-1
        while up <= down and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            
            for i in reversed(range(left,right+1)):
                ans.append(matrix[down][i])
            down -= 1
            
            for i in reversed(range(up,down+1)):
                ans.append(matrix[i][left])
            left += 1

        return ans[:(len(matrix) * len(matrix[0]))]

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))