#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 10:37:00
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 13:43:51

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        key = head.val
        p = head
        while p.next != None:
            p_after = p.next
            if p_after.val == key:
                p.next = p_after.next
            else:
                key = p_after.val
                p = p_after
        return head