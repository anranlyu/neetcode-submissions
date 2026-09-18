class Solution:
    def findMin(self, nums: List[int]) -> int:
        i , j = 0 , len(nums) - 1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] <= nums[j]:
                if mid == 0 or nums[mid-1]>nums[mid]:
                    return nums[mid]
                j = mid - 1
            else:
                i = mid +1
        return nums[i]