class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        for x , y in points:
            d= x*x + y*y
            pairs.append((d,x,y))
        
        heapq.heapify(pairs)
        res = []
        for _ in range(k):
            d,x,y = heapq.heappop(pairs)
            res.append([x,y])
        

        return res