# -*- coding: utf-8 -*-
# @Author: zhanglz
# @Date:   2018-05-11 21:43:41
# @Last Modified by:   zhlz_home
# @Last Modified time: 2018-05-11 21:44:43

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
对于每一个节点，通过checkDepth方法递归获得左右子树的深度，
如果子树是平衡的，则返回真实的深度，若不平衡，直接返回-1，
此方法时间复杂度O(N)，空间复杂度O(H)
"""
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkDepth(root):
            if not root:
                return 0
            left = checkDepth(root.left)
            if left == -1:
                return -1
            right = checkDepth(root.right)
            if right == -1:
                return -1
            diff = abs(left - right)
            if diff > 1:
                return -1
            else:
                return 1 + max(left, right)
        
        if checkDepth(root) == -1:
            return False
        else:
            return True