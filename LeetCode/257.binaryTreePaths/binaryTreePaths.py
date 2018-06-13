#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-13 09:07:12
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 09:10:39

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path, res):
            if root:
                path.append(str(root.val))
                left = dfs(root.left, path, res)
                right = dfs(root.right, path, res)
                if not left and not right:
                    res.append('->'.join(path))
                path.pop()
                return True
        ans = []
        dfs(root, [], ans)
        return ans