class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list() # pair(index,height)
        max_area = 0

        for i , v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
                start = index
            stack.append((start, v))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
