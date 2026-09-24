class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)


        l = 0
        best = 0

        for r in range(len(s)):
            count[s[r]] += 1  # expand: s[r] enters

            while (r - l + 1) - max(count.values()) > k:  # too many replacements needed
                count[s[l]] -= 1  # shrink: s[l] leaves
                l += 1

            best = max(best, r - l + 1)  # window is valid now

        return best
