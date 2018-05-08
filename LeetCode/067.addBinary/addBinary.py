#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-08 15:54:07
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-08 17:42:51

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #sum = int(a,2) + int(b,2)
        #print(sum)
        #return bin(sum)[2:]
        
        list_a = list(a)
        list_b = list(b)
        list_a.reverse()
        list_b.reverse()
        carry = False
        while len(list_a) < len(list_b):
            list_a.append('0')
        while len(list_a) > len(list_b):
            list_b.append('0')
        
        for i in range(0,len(list_a)):
            if list_a[i] == list_b[i]:
                if carry:
                    list_a[i] = '1'
                    carry = False
                else:
                    list_a[i] = '0'
                if list_b[i] == '1':
                    carry = True
            else:
                if carry:
                    list_a[i] = '0'
                    carry = True
                else:
                    list_a[i] = '1'
                    carry = False
        if carry:
            list_a.append('1')
        list_a.reverse()
        return ''.join(list_a).lstrip('0')

if __name__ == '__main__':
    sol = Solution()
    str_a = '111'
    str_b = '01'
    print(sol.addBinary(str_a,str_b))