"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
From Akashdeep Singh to Everyone: (7:24 PM)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.itemssum = 0
        self.items = []
        

    def next(self, val: int) -> float:

        if len(self.items) == self.size:
            self.sum = self.sum - self.items[0]
            del self.items[0]
            self.items.append(val)
            self.sum = self.sum + val
            return self.itemssum/self.size
        else:
            self.items.append(val)
            return sum(self.items)/len(self.items)
