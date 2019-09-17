import sys

def solution() :
    N = int(sys.stdin.readline())
    num_list = []
    for _ in range(N) :
        num_list.append(list(map(int, sys.stdin.readline().split())))

    num_list.sort()

    for i in num_list :
        print(i[0], end=' ')
        print(i[1])
    
solution()
