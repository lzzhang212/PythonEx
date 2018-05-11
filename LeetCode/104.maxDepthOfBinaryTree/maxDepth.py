#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-10 15:25:46
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-10 15:30:21

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.tailMaxDepth(root,1)
        return self.depth

    def tailMaxDepth(self, node, deep):
        if not node:
            return None
        if self.depth < deep:
            self.depth += 1
        self.tailMaxDepth(node.right, deep+1)
        self.tailMaxDepth(node.left, deep+1)
