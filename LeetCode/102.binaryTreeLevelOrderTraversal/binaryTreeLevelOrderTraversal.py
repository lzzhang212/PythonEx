#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 11:20:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 13:14:40

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        ans = [[root.val]]
        while queue:
            levelans = []
            for _ in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                    levelans.append(root.left.val)
                if root.right:
                    queue.append(root.right)
                    levelans.append(root.right.val)
            if levelans:
                ans.append(levelans)
        return ans
