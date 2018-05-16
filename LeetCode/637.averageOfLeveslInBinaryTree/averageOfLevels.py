#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 13:14:51
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 13:21:06

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0
        queue = deque([root])      #deque(root)报错TypeError: 'TreeNode' object is not iterable
        ans = [float(root.val)]
        while queue:
            levelCount = 0
            levelSum = 0
            for _ in range(0, len(queue)):
                root = queue.popleft()
                if root.left:
                    levelCount += 1
                    levelSum += root.left.val
                    queue.append(root.left)
                if root.right:
                    levelCount += 1
                    levelSum += root.right.val
                    queue.append(root.right)
            if levelCount:
                ans.append(float(levelSum/levelCount))
        return ans
