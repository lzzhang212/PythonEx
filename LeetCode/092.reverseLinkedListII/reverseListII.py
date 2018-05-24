#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-23 14:51:02
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-23 14:51:04

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, p = dummy, head
        m_head = m_pre = None
        count = 0
        while p:
            count += 1
            if count > n:
                break
            if count >= m:
                if count == m:
                    m_head = p
                    m_pre = pre
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            else:
                p = p.next
                pre = pre.next
        m_head.next = p
        m_pre.next = pre
        return dummy.next