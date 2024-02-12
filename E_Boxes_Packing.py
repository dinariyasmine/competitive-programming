def min_visible_boxes(n, side_length):
    side_length.sort()
    left = 0
    for right in range(n):
        if side_length[right] > side_length[left]:
            left += 1
    return (right - left + 1)

n = int(input().strip())
side_length = list(map(int, input().strip().split()))
result = min_visible_boxes(n, side_length)
print(result)
