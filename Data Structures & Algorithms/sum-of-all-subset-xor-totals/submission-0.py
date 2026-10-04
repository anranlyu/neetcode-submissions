class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        cur = 0

        def dfs(i):
            nonlocal cur, res
            if i >= len(nums):
                res += cur
                return
            
            cur ^= nums[i]
            dfs(i+1)
            cur ^= nums[i]
            dfs(i+1)
        dfs(0)
        return res