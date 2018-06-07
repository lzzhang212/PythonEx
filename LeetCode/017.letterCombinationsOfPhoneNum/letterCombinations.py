#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-06 15:50:59
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-06 16:16:53

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        def dfs(index, d, path, ans, digits):
            if index == len(digits):
                ans.append(''.join(path))
                return

            digit = int(digits[index])
            for c in d.get(digit, []):
                path.append(c)
                dfs(index+1, d, path, ans, digits)
                path.pop()
        ans = []
        dfs(0, d, [], ans, digits)
        return ans