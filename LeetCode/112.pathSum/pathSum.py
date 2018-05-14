#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 17:07:44
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 17:07:49

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        t = sum - root.val
        if not root.left and not root.right:
            return t == 0
        return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)