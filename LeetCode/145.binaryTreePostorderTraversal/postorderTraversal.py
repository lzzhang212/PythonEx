#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-13 11:01:11
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-13 11:03:01

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack1 = []
        stack2 = []
        ans = []
        stack1.append(root)
        while stack1:
            tempNode = stack1.pop()
            if tempNode.left:
                stack1.append(tempNode.left)
            if tempNode.right:
                stack1.append(tempNode.right)
            stack2.append(tempNode)
        while stack2:
            tempNode = stakc2.pop()
            ans.append(tempNode.val)
        return ans