def problem_2(str):
    stack = []
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