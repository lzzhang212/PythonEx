#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-11 10:20:28
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-11 10:36:05

from queue import Queue
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = Queue(0)  #Queue(maxsize):maxsize<=0表示队列尺寸无限制
        q.put(root)
        ans = [[root.val]]
        while q.qsize():
            ans_level = []
            for _ in range(0,q.qsize()):
                curNode = q.get()
                if curNode.left:
                    ans_level.append(curNode.left.val)
                    q.put(curNode.left)
                if curNode.right:
                    ans_level.append(curNode.right.val)
                    q.put(curNode.right)
            if ans_level:
                ans.append(ans_level)
        return ans[::-1]
                