#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-04-24 11:32:13
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-04-25 13:56:02

class MyStack(object):
    def __init__(self,size = 8):
        self.top = -1
        self.size = size
        self.stack = []

    def __str__(self):
        return str(self.top_value)

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top + 1 == self.size:
            return True
        return False

    def top(self):
        if self.is_empty() == True:
            raise Exception('StackIsEmpty!',end = '\n')
        return self.stack[self.top] 

    def push(self, data):
        if self.is_full() == True:
            raise Exception('StackIsFull!', end = '\n')
        else:
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if self.is_empty() == True:
            raise Exception('StackIsEmpty', end = '\n')
        else:
            self.top -= 1
            return self.stack.pop()

    def show(self):
        print(self.stack)

if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push('a')
    stack.push('b')
    stack.push(5)
    stack.push(6)
    stack.show()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.is_empty())
    print(stack.is_full())
    print(stack.top)
    stack.show()

