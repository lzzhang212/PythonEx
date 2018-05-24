#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-23 15:19:06
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-23 16:12:26

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
            if not head or not head.next:
                return head
            p = head
            pre = None
            while p:
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            return pre
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        p1, p2 = l1, l2
        carry = 0
        while p1 and p2:
            p1.val = p1.val + p2.val + carry
            if p1.val > 9:
                p1.val %= 10
                carry = 1
            else:
                carry = 0
            pre1 = p1
            p1 = p1.next
            p2 = p2.next
        if p2:
            pre1.next = p2
        while pre1.next:
            pre1.next.val += carry
            if pre1.next.val > 9:
                pre1.next.val %= 10
                carry = 1
                pre1 = pre1.next
            else:
                carry = 0
                break
        if carry == 1:
            end = ListNode(1)
            pre1.next = end
        l1 = reverseList(l1)
        return l1