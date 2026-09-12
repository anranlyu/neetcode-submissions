class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list()
        for i in range(len(position)):
            pair.append([position[i],(target - position[i])/speed[i]])
        
        pair.sort(reverse=True)

        fleet = 0
        slowest = 0

        for i, v in pair:
            if fleet == 0:
                fleet = 1
                slowest = v
            else:
                if v > slowest:
                    fleet+=1
                    slowest = v
        return fleet
                    





'''
(x-p1)/s1 = (x-p2)/s2
s2x-s2p1=s1x-s1p2
(s2-s1)x = s2p1-s1p2
x=(s2p1-s1p2)/(s2-s1)
'''