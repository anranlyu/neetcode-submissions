class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashmap1 = Counter(s1)
        hashmap2 = defaultdict(int)

        k  = len(s1)

        for r in range(len(s2)):
            
            hashmap2[s2[r]]+=1

            if r>= k:
                if hashmap2[s2[r-k]]>1:
                    hashmap2[s2[r-k]] -=1
                else:
                    del hashmap2[s2[r-k]]

            if r >= k - 1:
                if hashmap1 == hashmap2:
                    return True
            
        return False


            
        