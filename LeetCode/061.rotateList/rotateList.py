#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 10:45:33
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 10:45:35

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        length = 1
        while p.next:
            length += 1
            p = p.next
        p.next = head
        k %= length
        for _ in range(length - k):
            p = p.next
            head = head.next
        p.next = None
        return head