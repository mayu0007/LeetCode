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

# Method 2: The min stack only store current min value 
# Additional Space: O(N)
class MinStack_v2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)
        # push the element to minStack if it is the current min 
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)      

    def pop(self) -> None:
       if len(self.mainStack):
            deleted = self.mainStack.pop()
            if deleted == self.minStack[-1]:
                self.minStack.pop()     

    def top(self) -> int:
        if len(self.mainStack):
            return self.mainStack[-1] 
        
    def getMin(self) -> int:
        if len(self.minStack):
            return self.minStack[-1]

# Method 2: Stack each element is a tuple (value, current_min)
# Additional Space: O(N) 
class MinStack_v3:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        # Store current element, current min tuple
        if self.stack: 
            self.stack.append((x,min(self.getMin(),x)))
        else:
            self.stack.append((x,x))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop() 

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

# Method 4: Use an variable to store the current min, prev min 
# Additional Space: O(1)
class MinStack_v4:
     
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = None

    def push(self, x: int) -> None:

        if not self.stack:
            self.minimum = x 
            self.stack.append(x)
        elif x >= self.minimum:
            self.stack.append(x)
        elif x < self.minimum:
            temp = 2 * x - self.minimum  # temp < minimum
            self.stack.append(temp)
            self.minimum = x
                    
    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped < self.minimum:
                self.minimum = 2*self.minimum - popped
                return (popped + self.minimum) // 2
            
    def top(self) -> int:
        if self.stack:
            if self.stack[-1] < self.minimum:
                return self.minimum
            else:
                return self.stack[-1]
    def getMin(self) -> int:
        return self.minimum
