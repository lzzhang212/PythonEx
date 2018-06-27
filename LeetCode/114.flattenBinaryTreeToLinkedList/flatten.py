#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-22 08:46:42
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-22 08:55:12

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(root, res):
            if not root:
                res.append(root)
                inorder(root.left, res)
                inorder(root.right, res)
        res = []
        inorder(root, res)
        if not res or len(res) == 1:
            return
        tmp_node = root
        for i in range(1, len(res)):
            tmp_node.right = res[i]
            tmp_node.left = None
            tmp_node = res[i]
        