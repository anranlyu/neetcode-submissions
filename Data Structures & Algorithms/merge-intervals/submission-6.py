class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for s,e in intervals[1:]:
            if s <= merged[-1][1]:
                merged[-1][1] = max(e,merged[-1][1])
                merged[-1][0] = min(s,merged[-1][0])
            else:
                merged.append([s,e])
        return merged

        