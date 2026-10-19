class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                if helper(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
            
        def helper(string:str) -> bool:
            i , j = 0 , len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i+=1
                j-=1
            return True
        
        dfs(0)
        return res