def min_visible_boxes(n, boxes):
    boxes.sort() 
    visible = 0

    
    for i in range(n):
        can_be_packed = True
        for j in range(i + 1, n):
            if boxes[i] < boxes[j]:
                can_be_packed = False
                break
        if can_be_packed:
            visible += 1

    return visible


n = int(input().strip())
lines = list(map(int, input().strip().split()))
result = min_visible_boxes(n, lines)
print(result)
