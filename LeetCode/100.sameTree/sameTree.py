#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-10 09:57:04
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-10 13:59:39
from quque import Queue
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

#迭代版本，利用队列对二叉树进行广度优先遍历
    def isSameTreeNR(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        que1 = Queue()
        que2 = Queue()
        curNode1 = p
        curNode2 = q
        que1.put(curNode1)
        que2.put(curNode2)

        while not que1.empty() and not que2.empty():
            curNode1 = que1.get()
            curNode2 = que2.get()
            if curNode1.val != curNode2.val:
                return False
            if curNode1.left and curNode2.left:
                que1.put(curNode1.left)
                que2.put(curNode2.left)
            if curNode1.right and curNode2.right:
                que1.put(curNode1.right)
                que2.put(curNode2.right)
            if (curNode1.left and not curNode2.left) or (not curNode1.left and curNode2.left):
                return False
            if (curNode1.right and not curNode2.right) or (not curNode1.right and curNode2.right):
                return False
        return True



