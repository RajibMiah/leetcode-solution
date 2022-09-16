def isValid(s):
    stack = []
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        elif ch == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()
        elif ch == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(isValid("()[]{}"))  # Output: true
