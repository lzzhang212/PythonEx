#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-01 10:41:44
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-01 10:46:27

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, path, res, n):
            if len(path) == 2*n:
                if left == 0:
                    res.append("".join(path))
                return

            if left < n:
                path.append("(")
                dfs(left+1, path, res, n)
                path.pop()
            if left > 0:
                path.append(")")
                dfs(left-1, path, res, n)
                path.pop()
        res = []
        dfs(0, [], res, n)
        return res