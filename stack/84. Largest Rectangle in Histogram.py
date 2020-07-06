# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1
# find the area of largest rectangle in the histogram.
from typing import List


def largestRectangleArea(self, heights: List[int]) -> int:

    # append an zero at the end of the height
    # so that we will always have a smaller height at the end
    heights.append(0)

    # stack will never be empty
    stack = [-1]

    ans = 0

    for i in range(len(heights)):

        # whenever the new height is smaller than top of stack,
        # we can determine the area bounded by the top of stack
        # and we pop the old height from our stack
        # stack[-1]: top of stack
        # stack.pop(): bottom of stack
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)

        # we still cannot determine the area bounded by heights in stack
        stack.append(i)

    heights.pop()
    return ans