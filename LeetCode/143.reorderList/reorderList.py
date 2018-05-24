#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-24 08:59:10
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-24 09:58:16

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            if not head or not head.next:
                return head
            cur = head
            pre = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        if not head or not head.next:
            return None

        #长度为偶数时，fast指向None，slow指向第2/n + 1个节点
        #长度为奇数时，fast指向最后一个节点，slow指向中间节点
        fast = slow = pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        slow = reverseList(slow)
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = slow
            slow = slow.next
            cur.next.next = tmp
            cur = tmp
        cur.next = slow