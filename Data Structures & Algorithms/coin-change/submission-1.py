class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(a):
            if a == 0:
                return 0
            if a < 0:
                return -1
            if a in memo:
                return memo[a]

            best = float('inf')
            for c in coins:
                sub = dfs(a - c)
                if sub != -1:
                    best = min(best, sub + 1)

            memo[a] = -1 if best == float('inf') else best
            return memo[a]
        
        return dfs(amount)