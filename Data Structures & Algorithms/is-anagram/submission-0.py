class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for x in s:
            if a.get(x) == None:
                a[x] = 1
            else:
                a[x] +=1
        
        for y in t:
            if b.get(y) ==None:
                b[y] =1
            else:
                b[y] +=1
        
        return a == b
        