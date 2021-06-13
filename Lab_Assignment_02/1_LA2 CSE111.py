import math
def divide(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return math.modf(a/b)[0]

print(divide(int(input()), int(input())))