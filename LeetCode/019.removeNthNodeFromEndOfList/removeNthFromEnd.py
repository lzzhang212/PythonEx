#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 11:25:37
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 11:27:33

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        first = second = head
        while first.next:
            n -= 1
            first = first.next
            if n <= 0:
                pre = second
                second = second.next
        if second == head:
            head = head.next
        else:
            pre.next = pre.next.next
        return head