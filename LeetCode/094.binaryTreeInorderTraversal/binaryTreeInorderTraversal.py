#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-13 09:55:42
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 09:56:54

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                t = stack.pop()
                res.append(t.val)
                root = t.right
        return res