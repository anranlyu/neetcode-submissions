class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        low, high = 1 , max(piles)
        cur = 0

        while low <= high:
            mid = (low+high)//2
            hour = self.helper(mid,piles)
            if hour > h:
                low = mid + 1
            elif hour <= h:
                high = mid -1
                cur = mid
        return cur


    def helper(self,rate,piles) -> int:
        time = 0
        for p in piles:
            time += (p+rate-1) // rate
        return time

        

        