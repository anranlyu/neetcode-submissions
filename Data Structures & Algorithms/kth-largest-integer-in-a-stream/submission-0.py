import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = list(nums)      # no heapify needed — nlargest doesn't require a heap
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]
