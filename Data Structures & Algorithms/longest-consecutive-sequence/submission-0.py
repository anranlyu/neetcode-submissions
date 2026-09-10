class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hnums = set(nums)
        s = defaultdict(list)

        for x in hnums:
            if x-1 not in hnums:
                s[x].append(x)
        
        for i in s:
            value = i + 1
            while value in hnums:
                s[i].append(value)
                value +=1
            i+=1
        
        length = 0

        for x in s.values():
            if len(x) > length:
                length = len(x)
        return length

