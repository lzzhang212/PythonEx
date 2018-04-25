#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-04-25 14:08:49
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-04-25 16:13:57

class MyQueue(object):
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = []

    def enqueue(self, value):
        if self.is_full() == True:
            raise Exception('QueueIsFull!')
        else:
            self.rear += 1
            self.queue.append(value)

    def dequeue(self):
        if self.is_empty() == True:
            raise Exception('QueueIsEmpty!')
        else:
            self.front += 1
            return self.queue.pop(0)

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear - self.front + 1) == self.size

    def show(self):
        print(self.queue)

if __name__ == '__main__':
    q = MyQueue(10)
    for i in range(9):
        q.enqueue(i)
    q.show()
    print(q.rear,q.front)
#    q.enqueue(100)
    print(q.is_empty())
    print(q.is_full())
    for i in range(3):
        q.dequeue()
    q.show()
    print(q.is_empty())

