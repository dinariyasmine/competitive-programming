def B_drink(n, drinks):
    orange_percentage = sum(drinks)
    global_percentage = orange_percentage / n
    return global_percentage

n = int(input().strip())
drinks = list(map(int, input().strip().split()))
result = B_drink(n, drinks)
print("{:.12f}".format(result))
