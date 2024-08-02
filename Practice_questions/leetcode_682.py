class Solution:
    def calPoints(self, operations : List[str]) -> int:
        stack = []

        for op in operations:
            if(op == "+"):
                stack.append(stack[-1] + stack[-2])
            elif(op == "D" or op == "d"):
                stack.append(stack[-1] * 2)
            elif(op == "C" or op == "c"):
                stack.pop
            else:
                stack.append(int(op))
        return sum(stack)