if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
    
    
    students.sort(key=lambda x: x[1])
    
    
    second_lowest_score = None
    for s in students:
        if second_lowest_score is None:
            second_lowest_score = s[1]
        elif s[1] > second_lowest_score:
            second_lowest_score = s[1]
            break
    
    
    second_lowest_students = [s[0] for s in students if s[1] == second_lowest_score]
    
    
    second_lowest_students.sort()
    
    
    for name in second_lowest_students:
        print(name)
