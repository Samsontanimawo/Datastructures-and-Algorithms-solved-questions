from collections import deque

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.sum_window = 0.0

    def next(self, val):
        # If the window size is reached, pop the oldest element from the window
        if len(self.window) == self.size:
            self.sum_window -= self.window.popleft()

        # Add the new value to the window and update the sum
        self.window.append(val)
        self.sum_window += val

        # Calculate and return the moving average
        return self.sum_window / len(self.window)