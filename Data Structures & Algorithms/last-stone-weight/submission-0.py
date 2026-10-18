class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a != b:
                heapq.heappush_max(stones,a-b)
        

        return - stones[0] if stones else 0