#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-15 11:31:21
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-15 13:32:57

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ans = []
        length = len(nums)
        for k in range(0, length):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = length - 1
            target = 0 - nums[k]
            while i < j:
                if (nums[i] + nums[j]) == target:
                    ans.append((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))