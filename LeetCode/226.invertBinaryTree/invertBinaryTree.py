#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 18:12:27
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 18:13:36

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.invertTree(self.left)
        self.invertTree(self.right)
        root.left, root.right = root.right, root.left
        return root