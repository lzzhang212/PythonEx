#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-15 20:13:04
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-15 20:18:06

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        res = pre
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            first.next = second.next
            second.next = first
            pre.next = second
            pre = pre.next.next
        return res.next
