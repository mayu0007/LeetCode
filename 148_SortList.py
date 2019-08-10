#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 08:31:30 2019
148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

credit: https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
@author: my
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Method 1: Recursive Merge Sort 
# Time: Divide: logN Merge: Each level O(N) - NlogN
# Space: 
# Array - Edit Linked List reference node - no additional space
# Recursion - O(logN) Stack space for recursive call
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        # slow: mid point if odd length, mid - 1 if even
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None 
        left, right = self.sortList(head), self.sortList(mid)

        #Merge 2 sorted Linked List
        res = cur = ListNode(0)
        while left and right:
            if left.val < right.val: cur.next, left = left, left.next
            else: cur.next, right = right, right.next
            cur = cur.next
        cur.next = left if left else right
        return res.next

