# Algorithm
# simply loop through every character.
# if an open braces is found then increase the count.
# if you find an operator then it means that expression is valid.so decrement the count.
# once the loop is completed then check..
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
