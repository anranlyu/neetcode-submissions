class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)    
        dp = [0] * (n+1)
        dp[1] = nums[0]
        res = dp[1]

        for i in range(2,n+1):
            dp[i] = max((dp[i-2] + nums[i-1]),(dp[i-1]))
            if res < dp[i]:
                res = dp[i]
        return res
        


