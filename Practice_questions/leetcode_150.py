#Evaluate Reveerse polish notation
#input  = ["1","2","+","3","*"]
#explanation = ((1+2)*3) = 9

def evalRPN(tokens: list[str]) -> int :
    stack = []
    for c in tokens:
        if (c == "+"):
            stack.append(stack.pop() + stack.pop())
        elif(c == "-"):
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        
        elif(c == "/"):
            a,b = stack.pop(),stack.pop()
            stack.append(b/a)
        
        elif (c == "*"):
            stack.append(stack.pop() * stack.pop())
        
        else:
            stack.append(int(c))
    return stack[0]

if __name__ == "__main__":
   input  = ["1","2","+","3","*"]
   print(evalRPN(input))

        
        