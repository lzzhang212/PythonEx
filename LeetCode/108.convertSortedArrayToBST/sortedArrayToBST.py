#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-11 11:28:06
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-11 14:27:03

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        midPos = len(nums)//2
        mid = nums[midPos]
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:midPos])
        root.right = self.sortedArrayToBST(nums[midPos+1:])
        return root