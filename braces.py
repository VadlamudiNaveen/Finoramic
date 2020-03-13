def braces(self, data):
    count = 0
    for char in data:
        if char == '(':
            count += 1
        elif char in '+-*/':
            count -= 1
        if count < 0:
            count = 0
    if count == 0:
        return 0
    return 1