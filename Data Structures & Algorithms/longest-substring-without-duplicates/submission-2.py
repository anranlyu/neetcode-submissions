class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l= r= maxim = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            
            else:
                seen.add(s[r])
                maxim = max(maxim, (r-l+1))
                r+=1

        return maxim