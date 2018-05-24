#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-23 17:02:24
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-23 17:02:28

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
        p1, p2 = l1, l2
        num1 = num2 = 0
        while p1:
            num1 = num1*10 + p1.val
            p1 = p1.next
        while p2:
            num2 = num2*10 + p2.val
            p2 = p2.next
        num = num1 + num2
        cur = head = ListNode(0)
        while num:
            cur.val = num%10
            num //= 10
            if num:
                tmp = ListNode(0)
                tmp.next = cur
                cur = tmp
        return cur