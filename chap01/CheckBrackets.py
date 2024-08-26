# 괄호 검사 프로그램
from StackClass import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == ')' and left != '('):
                    return False
    
    return stack.isEmpty()

print(checkBrackets("{ A[(i+1)]=0; }"))
print(checkBrackets("if ((x<0) && (y<3)"))
print(checkBrackets("while (n<8)) {n++;}"))        
print(checkBrackets("arr[(i+1)=0;"))
