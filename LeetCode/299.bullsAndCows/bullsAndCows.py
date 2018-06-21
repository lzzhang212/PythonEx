#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lzzhang
# @Date:   2018-06-21 17:48:13
# @Last Modified by:   lzzhang
# @Last Modified time: 2018-06-21 17:55:16

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guess = list(guess)
        countA = 0
        countB = 0
        d = {}
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                countA += 1
            if secret[i] not in d:
                d[secret[i]] = 1
            else:
                d[secret[i]] += 1
        for i in range(len(guess)):
            if guess[i] in d:
                countB += 1
                d[guess[i]] -= 1
        return str(countA) + 'A' + str(countB-countA) + 'B'