class Solution:

    def computeString(self, string:str):
        counts = [0] * 26
        for c in string:
            counts[ord(c)-97] +=1
        return tuple(counts)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            count = self.computeString(string)
            if d.get(count) == None:
                d[count] = [string]
            else:
                d[count].append(string)
        return list(d.values())
        

        