#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-10 18:35:06
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-10 18:36:56

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = head = ListNode(-1)
        carry = 0
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            carry = p.next.val//10
            p.next.val = p.val%10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        res = l1 or l2
        while res:
            p.next = ListNode(res.val + carry)
            carry = p.next.val//10
            p.next.val %= 10
            p = p.next
            res = res.next
        if carry:
            p.next = ListNode(1)
        return head.next