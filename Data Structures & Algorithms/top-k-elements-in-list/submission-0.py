class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1

            else:
                hashmap[i] = 1
        
        l = sorted(hashmap.items(), key=lambda pair: pair[1], reverse=True)
        result = []
        for i in range(k-1,-1,-1):
            result.append(l[i][0])
        return result

        