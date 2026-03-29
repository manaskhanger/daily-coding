# Valid Parentheses (Easy)

def is_valid(s):
    stack = []
    m = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in m.values():
            stack.append(c)
        elif c in m:
            if not stack or stack.pop() != m[c]:
                return False
    return not stack