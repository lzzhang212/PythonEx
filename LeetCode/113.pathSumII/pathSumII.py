#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 17:08:26
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 17:09:10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, s, path, res):
            if root:
                path.append(root.val)
                s -= root.val
                left = dfs(root.left, s, path, res)
                right = dfs(root.right, s, path, res)
                if not left and not right and s==0:
                    res.append(path + [])  #此处不能传递path的引用
                path.pop()
                return True
        res = []
        dfs(root, sum, [], res)
        return res