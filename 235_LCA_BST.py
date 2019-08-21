#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:51:16 2019

@author: my
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Method 1: Use the property of BST: 
#the left subtree of node contains nodes with values less than or equal to the node's value 
#the right subtree of node contains nodes with values greater than to the node's value        
#Left and Right subtrees are BSTs.       
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        # right sub-tree
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # left sub-tree
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root