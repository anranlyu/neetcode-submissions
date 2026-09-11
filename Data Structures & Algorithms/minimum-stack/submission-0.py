class MinStack:

    def __init__(self):
        self.stack = list()
        self.order = list()

        

    def push(self, val: int) -> None:
        if not self.order:
            self.order.append(val)
        else:
            self.order.append(min(self.order[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.order.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.order[len(self.stack) - 1]

