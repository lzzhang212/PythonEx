#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 14:35:31
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 14:46:50

#基于贪心，有利润就卖出
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] > prices[i-1]:
                prifit += prices[i] - prices[i-1]

        return profit
