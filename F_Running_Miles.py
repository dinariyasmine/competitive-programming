def max_beauty(t, test_cases):
    for test_case in test_cases:
        n = test_case[0]
        beauties = test_case[1]
        
        max_sum = float('-inf')
        window_sum = sum(beauties[:3])
        
        for i in range(n - 2):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    beauty_sum = beauties[i] + beauties[j] + beauties[k] - (j - i)
                    max_sum = max(max_sum, beauty_sum)
        
        print(max_sum)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    beauties = list(map(int, input().split()))
    test_cases.append((n, beauties))

max_beauty(t, test_cases)
