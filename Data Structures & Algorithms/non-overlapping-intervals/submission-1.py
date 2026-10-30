class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        merged = []
        merged.append(intervals[0])
        count = 0

        for i in range(1,len(intervals)):
            if intervals[i][0] < merged[-1][1]:
                merged[-1] = intervals[i] if intervals[i][1] < merged[-1][1] else merged[-1]
                count += 1
            else:
                merged.append(intervals[i])
        return count
