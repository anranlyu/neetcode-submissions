class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            j=i
            dfs(i+1, total + nums[i])
            subset.pop()
            while j < len(nums) and nums[j] == nums[i]:
                j+=1
            dfs(j, total)
        dfs(0,0)
        return res

