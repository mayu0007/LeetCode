#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:50:29 2019
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
@author: my
"""
from typing import List
#Method 1: built in "sorted" method return a new sorted version of array, Timsort
# Time: O(NlogN) 
class Solution_v1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

#Method 2: Selection Sort
# Time: O(N*k)
class Solution_v2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            max_index = i
            for j in range(n,i,-1):
                if nums[j] > nums[max_index]:
                    max_index = j
            nums[i], nums[max_index] = nums[max_index], nums[i]
        return nums[k-1]

#Method 3: bubble sort
#Time: O(Nk)
class Solution_v3:        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums)-1,i,-1):
                if nums[j] > nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums[k-1]
#heap sort -  trees
        
#insertion sort 
#quicksort
#merge sort
