#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:06:15 2019
## Task 6: 78. Subsets
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
@author: my
"""


from typing import List

# Method 1: Bit Mask
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Number of subsets: 2^n
        n = 1 << len(nums)
        res = []
        
        for i in range(n):
            cur = []
            for j in range(len(sums)):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res

    