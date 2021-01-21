if __name__ == '__main__':
    N = int(input())
    s=[]
    for _ in range(N):
        text=list(input().split())
        if text[0]=="insert":
            strval="s.text[0](int(text[1]),int(text[2]))"
            exec(strval)
            print(s)
        elif text[0]=="print":
            print(s)
        elif text[0]=="remove":
            s.remove(int(text[1]))
        elif text[0]=="append":
            s.append(int(text[1]))
        elif text[0]=="sort":
            s.sort()
        elif text[0]=="pop":
            s.pop()
        elif text[0]=="reverse":
            s.reverse()
        