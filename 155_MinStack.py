# -*- coding: utf-8 -*-
"""
155. Min Stack
Design a stack that supports 
push, pop, top, and retrieving the minimum element in constant time.
"""

# Method 1: Use helper stack to store the current min element;
# Additional Space: O(N)

class MinStack_v1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)
        # push the current min to minStack
        if len(self.minStack) == 0 or self.minStack[-1] > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if len(self.mainStack):
            self.mainStack.pop()
            self.minStack.pop()    

    def top(self) -> int:
        if len(self.mainStack):
            return self.mainStack[-1]    

    def getMin(self) -> int:
        if len(self.minStack):
            return self.minStack[-1]
    



