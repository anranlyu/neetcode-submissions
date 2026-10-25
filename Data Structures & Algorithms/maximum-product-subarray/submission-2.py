class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mx = [0] * (n+1)
        mn = [0] *(n+1)
        res = mn[1] = mx[1] = nums[0]
        for i in range(2,n+1):
            candidates = (nums[i-1], mx[i-1] * nums[i-1] ,mn[i-1]*nums[i-1])
            mx[i] = max(candidates)
            mn[i] = min(candidates)
            res = max(res,mx[i])
            
        
        return res
