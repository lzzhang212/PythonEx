#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 14:42:24
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 14:43:36

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre =  p = None
       
        while cur:
            p = cur.next
            cur.next = pre
            pre = cur
            cur = p
        return pre

    def reverseListR(self, head):
        if not head or not head.next:
            return head

        ret = self.reverseListR(head.next)
        head.next.next = head
        head.next = None
        return ret