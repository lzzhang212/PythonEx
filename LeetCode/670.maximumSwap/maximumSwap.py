#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-12 18:45:25
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-12 18:55:34

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = []
        while num:
            nums.append(str(num%10))
            num //= 10
        nums.reverse()
        for i in range(len(nums)):
            maxRight = nums[i]
            max_j = i
            for j in range(i+1, len(nums)):
                if nums[j] >= maxRight:
                    maxRight = nums[j]
                    max_j = j
            if maxRight > nums[i]:
                nums[i], nums[max_j] = nums[max_j], nums[i]
                break
        return int(''.join(nums))

if __name__ == '__main__':
    sol = Solution()
    num = 2736
    print(sol.maximumSwap(num))