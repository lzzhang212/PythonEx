#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 14:47:16
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 14:56:00

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0 or lenght == 1:
            return 0
        firstProf = [0 for _ in range(length)]
        secondProf = [0 for _ in range(length)]
        minPrice = prices[0]
        maxPrice = prices[-1]

        for i in range(1,length):
            firstProf[i] = max(prices[i] - minPrice, firstProf[i-1])
            minPrice = min(prices[i], minPrice)

        for i in reversed(range(0, length-1)):
            secondProf[i] = max(maxPrice - prices[i], secondProf[i+1])
            maxPrice = max(prices[i], maxPrice)

        maxProfit = 0
        for i in range(length):
            maxProfit = max(maxProfit, firstProf[i]+secondProf[i])
        return maxProfit