#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-27 16:21:50
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-27 16:22:12

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def getPath(root, target, path):
            cur = root
            while cur:
                if cur.val == target.val:
                    path.append(cur)
                    break
                elif cur.val > target.val:
                    path.append(cur)
                    cur = cur.left
                else:
                    path.append(cur)
                    cur = cur.right                  
        path_p = []
        path_q = []
        getPath(root, p, path_p)
        getPath(root, q, path_q)
        for i in list(reversed(path_p)):
            for j in list(reversed(path_q)):
                if i.val == j.val:
                    return i