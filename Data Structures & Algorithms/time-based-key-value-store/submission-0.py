class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        array = self.timemap[key]

        low , high = 0 , len(array) - 1
        cur = ""

        while low <= high:
            mid = (low + high) // 2
            if array[mid][0] == timestamp:
                return array[mid][1]
            elif array[mid][0] < timestamp:
                low = mid + 1
                cur = array[mid][1] 
            else:
                high = mid - 1
        return cur



        
