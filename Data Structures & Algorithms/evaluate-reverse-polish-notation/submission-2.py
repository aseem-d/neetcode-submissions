class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv}

        stack = []

        for i in tokens:
            if i in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                result = (operators[i])(b, a)
                stack.append(result)
            
            else:
                stack.append(int(i))
        
        return int(stack.pop())



        