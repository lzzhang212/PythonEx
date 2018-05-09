#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-09 13:56:29
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-09 14:40:21

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #尾部填充法 复杂度O(M+N) 时间 O(1) 空间
        while m>0 and n>0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[n+m-1] = nums2[n-1]
                n -= 1
            else:
                nums1[n+m-1] = nums1[m-1]
                m -= 1
        #因为是在nums1的基础上更改，所以不用考虑m，需要
        #考虑的是n还没结束就已经终止，这时需要把剩余的n个数，
        #放到nums1前面
        if n > 0:
            nums1[0:n] = nums2[0:n]
            