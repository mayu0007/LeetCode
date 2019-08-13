#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:35:10 2019

@author: my

169. Majority Element
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

"""
from typing import List
#Method 1: Counting Based
#Method 1.1: Map time O(N); space: O(N)
class Solution_v1:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        N = len(nums)
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > N//2:
                return num

#Method 2: Randomization
# Time: on average O(N) Space: O(1)
class Solution_v2:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        random.seed(200)
        N = len(nums)
        while True:
            index = random.randrange(0,N)
            sample = nums[index]
            count = 0
            for num in nums:
                if num == sample:
                    count += 1
                    if count > N //2:
                        return sample

#Method 3: Voting Based 
#To-do

#Method 4:                         