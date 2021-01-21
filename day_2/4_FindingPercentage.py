 n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #student_marks=sorted(student_marks)
           
    query_name = input()
    query_marks= student_marks[query_name]
    query_Per = sum(query_marks)/len(query_marks)
    print("%.2f"%query_Per)
