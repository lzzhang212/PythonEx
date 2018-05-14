#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-14 14:33:51
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-14 14:34:57

#时间复杂度O(n),空间复杂度O(1)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = 0
        pre = prices[0]
        for i in range(1,len(prices)):
            pre = min(prices[i],pre)
            ans = max(prices[i]-pre,ans)
        return ans
        