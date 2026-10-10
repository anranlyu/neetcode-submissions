class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        n = len(nums)
        while i < n - k:
            if nums[i] == val:
                nums[i] = nums[n-k-1]
                nums[n-k-1] = val
                k+=1
            else:
                i+=1
        return n-k
