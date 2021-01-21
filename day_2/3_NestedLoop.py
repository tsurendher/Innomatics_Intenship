if __name__ == '__main__':
    nisted_list=[]
    marks_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks_list.append(score)
        nisted_list.append([name,score])
    
    marks_list=sorted(set(marks_list))
    nisted_list=sorted(nisted_list)
    for a in nisted_list:
        if a[1]==marks_list[1]:
            print(a[0])