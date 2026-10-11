class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                subset.append(nums[i])
                dfs()
                used[i] = False
                subset.pop()
        
        dfs()
        return res

        
            
            