#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-22 19:50:50
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-22 19:50:53

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        p = head
        while p:
            copy = RandomListNode(p.label)
            copy.next = p.next
            p.next = copy
            p = p.next.next
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        p = head
        copyHead = copy = head.next
        while p:
            p.next = copy.next
            p = copy.next
            copy.next = copy = p.next if p else None
        return copyHead