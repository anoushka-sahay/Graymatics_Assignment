def problem_2(str):
    stack = []
    
    # edge case if number of opening bracket is not equal to number of closing bracket then return False
    if str.count('(') != str.count(')'):
        return False
    if str.count('{') != str.count('}'):
        return False
    if str.count('[') != str.count(']'):
        return False
    
    #adding opening bracket in str to the stack. If we encounter a closing bracket then we remove the opening bracket of same kind from the stack
    for x in range(len(str)):
        if str[x] == '(' or str[x] == '{' or str[x] == '[':
            stack.append(str[x])
        if str[x] == ')':
            if len(stack) != 0 and stack[len(stack)-1] == '(':
                stack.pop()
        if str[x] == '}':
            if len(stack) != 0 and stack[len(stack)-1] == '{':
                stack.pop()
        if str[x] == "]":
            if len(stack) != 0 and stack[len(stack)-1] == "[":
                stack.pop()
                
    #if string is valid then its size will be zero because for each closing bracket we removed the opening bracket
    if len(stack) == 0:
        return True
    else:
        return False
    
# print(problem_2("()[]{}"))
# print(problem_2("([)]"))
# print(problem_2("{{[](}})"))
# print(problem_2("{[()]}"))
str = input("Enter the required string of brackets: ")
print(problem_2(str))
