#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-13 09:14:32
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 09:17:48

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s and t:
                return False
            if s and not t:
                return False
            if s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
        if not s or not t:
            return False
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)