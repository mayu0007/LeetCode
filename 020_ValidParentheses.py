#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.


Created on Mon Aug  5 08:57:26 2019

@author: my
"""
# Method: 
# use stack to record seen open brackets and pop when the matching closing bracket is encountered
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        seen = []
        for c in s:
            # If the character is open bracket, append to the stack
            if c in pairs.values():
                    seen.append(c)
            # If the character is closing bracket
            ## If the stack is empty, there is no matching open bracket seen before -- return false
            ## if the last open bracket is not matched -- return false
            elif c in pairs: 
                if len(seen) == 0 or seen.pop() != pairs[c]:
                    return False
            # If the character is not a valid bracket -- return false
            else:
                return False   
        # after the loop, if still have open brackets not matched -- return false
        return len(seen) == 0