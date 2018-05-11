# -*- coding: utf-8 -*-
# @Author: zhanglz
# @Date:   2018-05-11 22:38:52
# @Last Modified by:   zhanglz
# @Last Modified time: 2018-05-11 22:38:52

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def triangles():
            N = [1]
            while True:
                yield N
                N.append(0)
                N = [N[i-1]+N[i] for i in range(0,len(N))]

        ans = []
        for t in triangles():

            ans.append(t)
            numRows -= 1
            if numRows == 0:
                break
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(10))