if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr, reverse=True)
    runnerUpScore = None
    for element in sorted_arr:
        if element != sorted_arr[0]:
            runnerUpScore = element
            break
    print(runnerUpScore)
        