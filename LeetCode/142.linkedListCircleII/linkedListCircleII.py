#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-15 19:44:38
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-15 19:48:08

#碰撞点到连接点的距离=头指针到连接点的距离

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = finder = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while finder != slow:
                    finder = finder.next
                    slow = slow.next
                return finder
        return None