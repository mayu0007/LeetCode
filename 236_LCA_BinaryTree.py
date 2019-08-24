#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:45:54 2019

236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

@author: my
"""

# Method1: Recursion, devide and conquer

#Traverse the tree in a DF. The moment you encounter either of the nodes p or q, return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a True flag. It can also be the node which itself is one of p or q and for which one of the subtree recursions returns a True flag.

# Time: O(N), N=no. of nodes in the binary tree. for traversing the tree 
# Space: O(N) for recursive stacks: the height of a skewed binary tree could be N. 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Edge Condition
        # p or q not found in this branch
        if not root:
            return False
        # Bingo
        if root == p or root == q:
            return root
        
        # Divide: for each potential root, recurse
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # Conquer: based on p, q distribution
        return root or left or right
            
        