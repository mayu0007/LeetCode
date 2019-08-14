#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:43:45 2019
231. Power of Two

Given an integer, write a function to determine if it is a power of two.
@author: my
"""

#Method 1: n > 0 and binary representation of n contain only one bit 1 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n < 0: 
            return False
        while n > 0:
            if n & 1: 
                count += 1
            n = n >> 1
        return count == 1