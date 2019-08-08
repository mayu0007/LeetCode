#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:45:15 2019
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.
@author: my
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
#Method 1: Min-Heap of size k to retrieve min element among all list head in O(1)
#Time: O(logk) for push every element into the heap.total: O(Nlogk)
        
# heapq.heappush: O(logN) 
# heapq.heappop: O(logN)

# Space: min-heap: O(k)
        
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = cur = ListNode(0)
        pq = []
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        while pq:
            val, i,node = heapq.heappop(pq) #
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(pq, (node.val,i, node))
        return dummy.next
