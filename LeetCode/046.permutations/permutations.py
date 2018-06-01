#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-31 18:16:16
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-31 18:51:00

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set([])
        def permuteDFS(nums, path, res, visited):
            if len(path) == len(nums):
                #path+[]为新生成的list，否则添加原path的引用后面pop为空
                res.append(path +[])
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    permuteDFS(nums, path, res, visited)
                    path.pop()
                    visited.discard(i)
        
        permuteDFS(nums, [], res, visited)
        return res
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))