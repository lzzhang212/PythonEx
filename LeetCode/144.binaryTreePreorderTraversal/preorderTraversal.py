#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-13 10:25:46
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 10:27:31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_stack = []
        res = []
        node_stack.append(root)
        while node_stack:
            root = node_stack.pop()
            res.append(root.val)
            if root.right:
                node_stack.append(root.right)
            if root.left:
                node_stack.append(root.left)
        return res
