#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-08 09:29:41
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-08 10:01:50
import pdb
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}', '[':']'}
        list1 =[]
        
        for each in s:
            if each in d:
                list1.append(each)
            else:
                if len(list1) == 0 or d[list1.pop()] != each:
                    return False
        return len(list1) == 0

if __name__ == '__main__':
    sol = Solution()
    s1 = ''
    s2 = '()'
    s3 = '((()))(){[]({[]})}'
    print(s1,sol.isValid(s1))
    print(s2,sol.isValid(s2))
    print(s3,sol.isValid(s3))
