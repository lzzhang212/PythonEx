#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-10 14:31:19
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-10 15:13:46

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        dq = deque()
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        dq.appendleft(root.left)
        dq.append(root.right)
        while len(dq) != 0:
            rnode = dq.pop()
            lnode = dq.popleft()
            if rnode.val != lnode.val:
                return False
            if (not lnode.left and rnode.right) or (lnode.left and not rnode.right):
                return False
            if lnode.left:
                dq.appendleft(lnode.left)
                dq.append(rnode.right)
            if (not lnode.right and rnode.left) or (lnode.right and not rnode.left):
                return False
            if lnode.right:
                dq.appendleft(lnode.right)
                dq.append(rnode.left)
        return True

