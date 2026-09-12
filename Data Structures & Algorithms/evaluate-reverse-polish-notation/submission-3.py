import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ops = {'+': operator.add,'-': operator.sub,'*': operator.mul,'/':lambda a, b: int(a / b)}

        for x in tokens:
            if x not in ops:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[x](a, b))
        return stack[0]