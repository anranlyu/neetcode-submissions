class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += f'{len(string)}#{string}'
        return encoded

    # 5#hello#5world
            
    def decode(self, s: str) -> List[str]:
        decoded = list()
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j+=1
            num = int(s[i:j])
            decoded.append(s[j+1:num+j+1])
            i = 1 + j + num
        return decoded


