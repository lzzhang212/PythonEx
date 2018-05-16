#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-05-16 13:22:46
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-05-16 14:21:53

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = []
        self.stackB = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stackA:
            self.stackB.append(x)
        else:
            if x <= self.stackB[-1]:
                self.stackB.append(x)
        self.stackA.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stackB[-1] == self.stackA[-1]:
            self.stackB.pop()
        self.stackA.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stackA[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stackB:
            return self.stackB[-1]


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_3 = obj.getMin()
    obj.pop()
    param_4 = obj.top()
    param_5 = obj.getMin()
    print(param_3, param_4, param_5)