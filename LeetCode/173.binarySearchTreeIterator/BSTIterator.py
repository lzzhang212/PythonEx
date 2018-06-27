#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-22 10:06:47
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-22 10:09:19

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.nextmin = 0
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            top = self.stack[-1]
            self.nextmin = top.val
            cur = top.right
            self.stack.pop()
            if cur:
                self.stack.append(cur)
                while cur.left:
                    self.stack.append(cur.left)
                    cur = cur.left
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        return self.nextmin