class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        output = [0 for _ in range(len(nums))]
        for num in nums:
            count[num]+=1
        for i in range(1,len(count)):
            count[i] += count[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            output[count[nums[i]]-1] =  nums[i]
            count[nums[i]]-=1
        
        nums[:] = output
        
