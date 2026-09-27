class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,sum=0,0,0
        length = 100001

        while r < len(nums):
            sum+=nums[r]

            while sum >= target:
                length = min(length, r-l+1)
                sum-=nums[l]
                l+=1
            r+=1
        
        if length > 100000:
            return 0
        else:
            return length

                