#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-21 15:10:03
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-21 15:41:14

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a == list(reversed(a))

    """空间复杂度O(1)，从中间逆置单链表后从头尾遍历一次
    """
    def isPalindrome2(self, head):
        if not head or not head.next:
            return True
        
        def reverseList(root):
            if not root or not root.next:
                return root
            pre = None          #bug1:初始值不能为root
            cur = root
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        newHead = reverseList(slow)
        p1 = head
        p2 = newHead
        while p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        return True
