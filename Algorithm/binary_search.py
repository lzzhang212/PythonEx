#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-04-24 11:02:57
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-04-24 13:35:41

def binary_search(test_list,item):
    low = 0
    high = len(test_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess_item = test_list[mid]
        if guess_item == item:
            return mid
        if guess_item > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    my_list = [x for x in range(100)]
    print(binary_search(my_list,99))
    print(binary_search(my_list,-1))


