#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 15:34:35
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 15:35:56

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next
        return pa