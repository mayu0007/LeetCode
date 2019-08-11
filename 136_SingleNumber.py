#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:07:15 2019
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
@author: my
"""
#Method 1: XOR 
# x ^ x = 0
# x ^ y ^ y = x

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in nums[1:]:
            res = res ^ i 
        return res

