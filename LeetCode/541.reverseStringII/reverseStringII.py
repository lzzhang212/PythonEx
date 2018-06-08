#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-08 09:47:54
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-08 10:19:03

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """         
        # length = len(s)
        # left = length%(2*k)
        # count = length//(2*k)
        # ans = ''
        # start = 0
        # end = k
        # while count:
        #     temp = s[start:end]
        #     ans += temp[::-1] + s[start+k,end+k]
        #     start += 2*k
        #     end += 2*k
        # if left < k:
        #     temp = s[start:]
        #     ans += temp[::-1]
        # else:
        #     temp = s[start:end]
        #     ans += temp[::-1] + s[end:]
        # return ans

        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
        
if __name__ == '__main__':
    sol = Solution()
    s = 'abcdefg'
    k = 2
    print(sol.reverseStr(s,k))