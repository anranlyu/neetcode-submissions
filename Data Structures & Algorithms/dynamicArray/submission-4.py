class DynamicArray:
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i ]

    def set(self, i: int, n: int) -> None:
        self.array[i ] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.set(self.size, n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size ]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


        '''
            arry        size capacity
            []          0.    1
            [1].        1.   1
            [1,2,0,0]   2.   4
            [1,3,0,0].  2.   4
                        1
        '''
