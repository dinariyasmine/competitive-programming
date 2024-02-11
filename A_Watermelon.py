def can_divide_watermelon(w):
    if w < 4 or w % 2 != 0:
        return "NO"
    else:
        return "YES"

w = int(input().strip())
result = can_divide_watermelon(w)
print(result)
