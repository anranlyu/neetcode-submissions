class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[1] = nums[0]
        pd = [0] * (n)
        pd[1] = nums[1]

        for i in range(2, n):
            dp[i] = max((dp[i-2]+nums[i-1]),dp[i-1])
        for i in range(2,n):
            pd[i] = max((pd[i-2]+nums[i]),pd[i-1])
        return max(dp[-1],pd[-1])