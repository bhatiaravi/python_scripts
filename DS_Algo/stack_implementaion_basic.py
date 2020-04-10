class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) >= 1:
            self.stack = self.stack[:len(self.stack) - 1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        min = self.stack[0]
        for idx in range(len(self.stack)):
            if self.stack[idx] < min:
                min = self.stack[idx]
        return min
