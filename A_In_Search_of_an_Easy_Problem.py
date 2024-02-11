def easy_or_hard(n, answers):
    if 1 in answers:
        return "HARD"
    else:
        return "EASY"

n = int(input().strip())
answers = list(map(int, input().strip().split()))
result = easy_or_hard(n, answers)
print(result)
